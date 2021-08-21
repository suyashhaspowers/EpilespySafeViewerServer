import datetime
from azure.ai.anomalydetector import AnomalyDetectorClient
from azure.ai.anomalydetector.models import DetectRequest, TimeSeriesPoint
from azure.core.credentials import AzureKeyCredential

def getAnomalies(lums):
    SUBSCRIPTION_KEY = "21199d03ce704c5cb0279a09230f4d36"
    ANOMALY_DETECTOR_ENDPOINT = "https://epilepsysafeviewermvp.cognitiveservices.azure.com/"
    CLIENT = AnomalyDetectorClient(AzureKeyCredential(SUBSCRIPTION_KEY), ANOMALY_DETECTOR_ENDPOINT)

    series = []
    timestamps = []

    for i in range(1, len(lums) + 1):
        timestamps.append(datetime.datetime.fromtimestamp(i).isoformat() + "Z")

    for timestamp, lum in zip(timestamps, lums):
        series.append(TimeSeriesPoint(timestamp=timestamp, value=lum))
    request = DetectRequest(series=series, granularity='secondly', max_anomaly_ratio=0.49, sensitivity=95)

    response = None
    try:
        response = CLIENT.detect_entire_series(request)
    except Exception as e:
        print(e)
    except BaseException as e:
        print(e)

    if response is None or not response.is_anomaly:
        print('No anomalies were detected in the time series.')
        return []

    return response.is_anomaly