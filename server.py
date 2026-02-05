""" server.py """
from flask import Flask, render_template, request
from EmotionDetection.emotion_detection import emotion_detector

app = Flask(__name__)

@app.route("/")
def home():
    """ Landing Page """

    return render_template("index.html")

@app.route("/emotionDetector")
def emotion():

    """Analyze text and return emotion scores with a dominant emotion."""

    text_to_analyze = str(request.args.get('textToAnalyze'))

    result = emotion_detector(text_to_analyze)

    if result['dominant_emotion'] is None:
        return "Invalid text! Please try again!"

    anger, disgust, fear, joy, sadness, dom = (
        result[k] for k in ("anger", "disgust", "fear", "joy", "sadness", "dominant_emotion")
    )

    return (
        f"For the given statement, the system response is "
        f"'anger': {anger}, 'disgust': {disgust}, 'fear': {fear}, "
        f"'joy': {joy} and 'sadness': {sadness}. "
        f"The dominant emotion is {dom}."
    )
