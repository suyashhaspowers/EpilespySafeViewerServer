from flask import Flask, request, jsonify
import luminance_process
import anomalies_process
import azure_client
from flask_cors import CORS

app = Flask(__name__)
CORS(app)


@app.route('/get_potential_seizure_timestamps', methods=["POST"])
def get_potential_seizure_timestamps():
    url = request.args.get('url')
    file = luminance_process.download_youtube_video(url)
    lums = (luminance_process.analyse_video_luminance(file))

    lums_post = luminance_process.post_process_luminance(lums, 30)
    anomalies = azure_client.getAnomalies(lums_post)

    anomalies = anomalies_process.post_process_anomalies(anomalies)
    changes = anomalies_process.get_changes(anomalies)
    changes = anomalies_process.get_changes_in_video_time(changes, 30)
    return jsonify({
        "result": changes
    })
