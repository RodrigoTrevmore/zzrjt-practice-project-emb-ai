"""
this module call IA to analyze text
"""
import json
import requests



def sentiment_analyzer(text_to_analyse):
    """
    send the info to WATSON for analysis
    """
    url = 'https://sn-watson-sentiment-bert.labs.skills.network/v1/watson.runtime.nlp.v1/NlpService/SentimentPredict'
    headers =  {"grpc-metadata-mm-model-id": "sentiment_aggregated-bert-workflow_lang_multi_stock"}
    myobj = { "raw_document": { "text": text_to_analyse } }
    response = requests.post(url, json = myobj, headers=headers, timeout=5000)
    formatted_response = json.loads(response.text)

    label = None
    score = None

    if response.status_code == 200:

        label = formatted_response['documentSentiment']['label']
        score = formatted_response['documentSentiment']['score']

    elif response.status_code == 500:
        label = None
        score = None

    return {'label': label, 'score': score}

