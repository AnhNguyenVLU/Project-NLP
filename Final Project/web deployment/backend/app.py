from flask import Flask, request, jsonify
from model_pred import predict

app = Flask(__name__)
app.config['SECRET_KEY'] = 'sentimentAnalysisKey'

@app.route('/sentiment_prediction', methods=["GET", "POST"])
def index():
    text = request.json['text']
    predictions = predict(text)
    return jsonify({"predictions": predictions})

if __name__ == "__main__":
    app.run(debug=True)