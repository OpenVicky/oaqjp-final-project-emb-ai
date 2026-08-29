'''
These are imports required for the server
'''
from flask import Flask, render_template, request
from EmotionDetection.emotion_detection import emotion_detector

app = Flask("Emotion Detector")

@app.route("/emotionDetector")
def emote_detector():
    '''
    This function returns scores for different emotions for a given text input.
    It also specifies the dominant emotion.
    '''
    text_to_analyze = request.args.get('textToAnalyze')
    response = emotion_detector(text_to_analyze)
    if response['dominant_emotion'] == 'None':
        return_string = "Invalid text! Please try again!"
    else:
        return_string = (
            f"For the given statement, the system response is 'anger': {response['anger']},"
            f"'disgust': {response['disgust']},"
            f"'fear': {response['fear']},"
            f"'joy': {response['joy']} and 'sadness': {response['sadness']}."
            f"The dominant emotion is {response['dominant_emotion']}."
        )
    return return_string

@app.route("/")
def render_index_page():
    '''
    Renders the static page for the client UI
    '''
    return render_template('index.html')

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
