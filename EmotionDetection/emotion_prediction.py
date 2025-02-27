import requests
import json

def emotion_detector(text_to_analyze):
    res = requests.post(
        'https://sn-watson-emotion.labs.skills.network/v1/watson.runtime.nlp.v1/NlpService/EmotionPredict',
        headers={'grpc-metadata-mm-model-id': 'emotion_aggregated-workflow_lang_en_stock'},
        json={'raw_document': {'text': text_to_analyze}}
    )

    if res.status_code == 400:
        return {}
    elif res.status_code != 200:
        raise Exception(f'unhandled response. {res.status_code}')

    formatted_res = json.loads(res.text)
    predictions = formatted_res['emotionPredictions']
    if not predictions:
        raise Exception('emotion predictions is empty')

    emotion = predictions[0]['emotion']
    results = {
        'anger': emotion['anger'],
        'disgust': emotion['disgust'],
        'fear': emotion['fear'],
        'joy': emotion['joy'],
        'sadness': emotion['sadness']
    }
    results['dominent_emotion'] = max(results, key=results.get)

    return results