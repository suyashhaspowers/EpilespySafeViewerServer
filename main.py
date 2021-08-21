from flask import Flask
import luminance_process
import azure_client

app = Flask(__name__)


@app.route('/')
def hello():
    file = luminance_process.download_youtube_video("https://www.youtube.com/watch?v=atkD-beZ9oI")
    lums = (luminance_process.analyse_video_luminance(file))

    lums_post = luminance_process.post_process_luminance(lums, 30)
    anomalies = azure_client.getAnomalies(lums)

    for i in range(len(lums_post) - 1):
        print(lums_post[i], anomalies[i])
