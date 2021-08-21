import pytube
import hashlib
import os
import cv2
import numpy
from PIL import Image, ImageStat


def get_hash(s):
    hash_object = hashlib.md5(s.encode())
    return hash_object.hexdigest()

# Downloads youtube video from url and saves locally
def download_youtube_video(url):
    file_name = get_hash(url)
    file_path = './videos/' + file_name

    if os.path.exists(file_path + ".mp4"):
        return file_path + ".mp4"

    video = pytube.YouTube(url)
    stream = video.streams.first()
    stream.download('./videos/', file_name+".mp4")
    return file_path + ".mp4"

# Use opencv and pillow to obtain luminance data on a local video 
def analyse_video_luminance(file_path):
    lums = []
    cap = cv2.VideoCapture(file_path)
   
    while (cap.isOpened()):
        ret, frame = cap.read()

        if not ret:
            break

        im_pil = Image.fromarray(frame).convert('L')
        lum = ImageStat.Stat(im_pil).mean[0]
        lums.append(lum)

    cap.release()
    cv2.destroyAllWindows()

    return lums

# Normalizing dataset and post processing luminance data using numpy
def post_process_luminance(lums, fps):
    lums_grad = numpy.gradient(lums)
    lums_absgrad = abs(lums_grad)

    avg = sum(lums_absgrad)/len(lums_absgrad)
    lums_thresh_absgrad = [max(avg, val)-avg for val in lums_absgrad]

    sliding_window_size = 5
    num_points = len(lums_thresh_absgrad)
    
    lums_thresh_absgrad_movingsum = []
    for i in range(num_points):
        moving_sum = sum(lums_thresh_absgrad[max(0, i - sliding_window_size//2) : i + 1 + sliding_window_size//2])
        lums_thresh_absgrad_movingsum.append(moving_sum)
    return lums_thresh_absgrad_movingsum

def post_process_anomalies(fps, anomalies):
    anomalies_bucketed = []
    sliding_window_size = 10
    num_points = len(anomalies)
    
    for i in range(num_points):
        bucket_val = any(anomalies[max(0, i - sliding_window_size) : i])
        anomalies_bucketed.append(bucket_val)
    return anomalies_bucketed

def get_changes(anomalies):
    changes = []
    prev = None
    for indx, val in enumerate(anomalies):
        if prev != val:
            changes.append([indx, val])
            prev = val
    return changes


def get_changes_in_video_time(changes, fps):
    timePerFrame = 1.0/fps
    return [[change[0]*timePerFrame, change[1]] for change in changes]