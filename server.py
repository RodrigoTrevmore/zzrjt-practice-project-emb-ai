"""
server.py
this modulee contains the server part
"""

from flask import Flask, render_template, request
from SentimentAnalysis.sentiment_analysis import sentiment_analyzer

#Initiate the flask app : TODO
app = Flask("Sentiment Analyer")

@app.route("/sentimentAnalyzer")
def sent_analyzer():
    ''' This code receives the text from the HTML interface and 
        runs sentiment analysis over it using sentiment_analysis()
        function. The output returned shows the label and its confidence 
        score for the provided text.
    '''
    text_to_analyze = request.args.get('textToAnalyze')

    response = sentiment_analyzer(text_to_analyze)
    label = response['label']
    score = response['score']

    if label is None:
        return"Invalid Input! Try again."
    return f"The given text has identified as {label} with score of {score}."



@app.route("/")
def render_index_page():
    ''' This function initiates the rendering of the main application
        page over the Flask channel
    '''
    return render_template('index.html')


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
