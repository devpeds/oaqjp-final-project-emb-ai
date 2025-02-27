"""
Server implementation for final project of `Developing AI Applications with Python and Flask` course
"""

from flask import Flask, render_template, request
from EmotionDetection.emotion_prediction import emotion_detector

app = Flask(__name__)

@app.route('/')
def index():
    """render template 'index.html'"""
    return render_template('index.html')

@app.route('/emotionDetector')
def detect_emotion():
    """analyze emotion from the providen text"""
    text_to_analyze = request.args.get('textToAnalyze')
    emotion = emotion_detector(text_to_analyze)
    if not emotion:
        return "Invalid text! Please try again!"

    return (
        "For the given statement, the system response is"
        f"'anger': {emotion['anger']}, "
        f"'disgust': {emotion['disgust']}, 'fear': {emotion['fear']}, "
        f"'joy': {emotion['joy']} and 'sadness': {emotion['sadness']}. "
        f"The dominant emotion is <b>{emotion['dominent_emotion']}</b>"
    )

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)
