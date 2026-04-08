from flask import Flask, request
from EmotionDetection import emotion_detector

app = Flask(__name__)

@app.route("/")
def home():
    return "Emotion Detector API is running!"

@app.route("/emotionDetector")
def emotion_detector_route():
    text_to_analyze = request.args.get('textToAnalyze')

    # 🔥 Validasi input kosong (WAJIB untuk tugas 7)
    if text_to_analyze is None or text_to_analyze.strip() == "":
        return "Invalid text! Please try again.", 400

    result = emotion_detector(text_to_analyze)

    # 🔥 Kalau API gagal
    if result is None:
        return "Error processing request.", 500

    # 🔥 Format output sesuai requirement IBM
    response = (
        f"For the given statement, the system response is "
        f"'anger': {result['anger']}, "
        f"'disgust': {result['disgust']}, "
        f"'fear': {result['fear']}, "
        f"'joy': {result['joy']}, "
        f"'sadness': {result['sadness']}. "
        f"The dominant emotion is {result['dominant_emotion']}."
    )

    return response


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)