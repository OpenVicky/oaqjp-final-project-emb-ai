import requests
import json

def emotion_detector(text_to_analyze):
    URL = 'https://sn-watson-emotion.labs.skills.network/v1/watson.runtime.nlp.v1/NlpService/EmotionPredict'
    HEADER = {"grpc-metadata-mm-model-id": "emotion_aggregated-workflow_lang_en_stock"}
    MYOBJ = { "raw_document": { "text": text_to_analyze } }
    response = requests.post(URL, json = MYOBJ, headers = HEADER)
    if response.status_code == 200:
        formatted_response = json.loads(response.text)
        anger_score = formatted_response['emotionPredictions'][0]['emotion']['anger']
        disgust_score = formatted_response['emotionPredictions'][0]['emotion']['disgust']
        fear_score = formatted_response['emotionPredictions'][0]['emotion']['fear']
        joy_score = formatted_response['emotionPredictions'][0]['emotion']['joy']
        sadness_score = formatted_response['emotionPredictions'][0]['emotion']['sadness']
        max_score = max(anger_score, disgust_score, fear_score, joy_score, sadness_score)
        if anger_score == max_score:
            dominant_emotion = 'anger'
        elif disgust_score == max_score:
            dominant_emotion = 'disgust'
        elif fear_score == max_score:
            dominant_emotion = 'fear'
        elif joy_score == max_score:
            dominant_emotion = 'joy'
        else:
            dominant_emotion = 'sadness'
        return { 'anger': anger_score, 'disgust': disgust_score, 'fear': fear_score, 'joy': joy_score, 'sadness': sadness_score, 'dominant_emotion': dominant_emotion }
    elif response.status_code == 400:
        return { 'anger': 'None', 'disgust': 'None', 'fear': 'None', 'joy': 'None', 'sadness': 'None', 'dominant_emotion': 'None' }
