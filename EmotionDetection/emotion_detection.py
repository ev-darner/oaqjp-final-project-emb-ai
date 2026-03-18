import requests, json

# Function to analyze emotions in text
def emotion_detector(text_to_analyze):
    # URL and Headers for Watson NLP Library AI
    url = 'https://sn-watson-emotion.labs.skills.network/v1/watson.runtime.nlp.v1/NlpService/EmotionPredict'
    header = {"grpc-metadata-mm-model-id": "emotion_aggregated-workflow_lang_en_stock"}

    # Inputted json
    json_obj = { "raw_document": { "text": text_to_analyze } }
    
    # Send text and recieve response from AI
    response = requests.post(url, json = json_obj, headers=header)
    emotion_dict = {'anger': None, 'disgust': None, 'fear': None, 'joy': None, 'sadness': None, 'dominant_emotion': None}

    #Format and extract results from response
    if response.status_code == 200:
        res = response.text
        json_res = json.loads(res)
        anger = json_res['emotionPredictions'][0]['emotion']['anger']
        disgust = json_res['emotionPredictions'][0]['emotion']['disgust']
        fear = json_res['emotionPredictions'][0]['emotion']['fear']
        joy = json_res['emotionPredictions'][0]['emotion']['joy']
        sadness = json_res['emotionPredictions'][0]['emotion']['sadness']
        emotion_dict = {'anger': anger, 'disgust': disgust, 'fear': fear, 'joy': joy, 'sadness': sadness, 'dominant_emotion': 0}

        # Analyze which emotion is the most dominant
        dominant_emotion = max(emotion_dict, key=emotion_dict.get)
        emotion_dict['dominant_emotion'] = dominant_emotion

    # Error handling for blank or invalid entries
    if response.status_code == 500:
        emotion_dict = {'anger': None, 'disgust': None, 'fear': None, 'joy': None, 'sadness': None, 'dominant_emotion': None}

    # Return response
    return emotion_dict