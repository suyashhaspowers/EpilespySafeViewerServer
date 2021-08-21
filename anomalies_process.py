def post_process_anomalies(anomalies):
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