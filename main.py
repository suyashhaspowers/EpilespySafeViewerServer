from flask import Flask
import luminance_process
import azure_client


luminance_process.download_youtube_video("https://www.youtube.com/watch?v=TDjamEAMIgo&ab_channel=Simon%26TaliaClips")
lums = (luminance_process.analyse_video_luminance('./videos/db2b281fc64d5b778d351e6d453e3b7c.mp4'))
print("luminance values:", luminance_process.post_process_luminance(lums, 30))

print("anomalies:", azure_client.getAnomalies(lums))
