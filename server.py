from flask import Flask, render_template, request
from EmotionDetection.emotion_prediction import emotion_detector

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/emotionDetector')
def detect_emotion():
    text_to_analyze = request.args.get('textToAnalyze')
    emotion = emotion_detector(text_to_analyze)
    return (
        "For the given statement, the system response is"
        f"'anger': {emotion['anger']}, "
        f"'disgust': {emotion['disgust']}, 'fear': {emotion['fear']}, "
        f"'joy': {emotion['joy']} and 'sadness': {emotion['sadness']}. "
        f"The dominant emotion is <b>{emotion['dominent_emotion']}</b>"
    )

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)
