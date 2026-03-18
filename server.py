"""Server file for emotion detection app"""
from flask import Flask, render_template, request
from EmotionDetection.emotion_detection import emotion_detector

app = Flask(__name__)

@app.route("/emotionDetector")
def emot_detector():
    """Function to detect the emotions of inputted text"""
    text_to_analyze = request.args.get('textToAnalyze')
    res = emotion_detector(text_to_analyze)

    if res['dominant_emotion'] is None:
        return "Invalid text! Please try again!"

    emotions = ({
        'anger': res['anger'],
        'disgust': res['disgust'],
        'fear': res['fear'],
        'joy': res['joy'],
        'sadness': res['sadness']
        })
    dominant_emotion = res['dominant_emotion']

    return (
        f"For the given statement, the system response is {emotions}." 
        f"The dominant emotion is {dominant_emotion}."
    )

@app.route("/")
def render_page():
    """Renders the index page"""
    return render_template('index.html')

if __name__ == '__main__':
    app.run(port=5000)
