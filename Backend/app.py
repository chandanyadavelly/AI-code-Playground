from flask import Flask, request, jsonify
from flask_cors import CORS
import joblib

app = Flask(__name__)
CORS(app)

# Load ML files
model = joblib.load("../ML/model.pkl")
vectorizer = joblib.load("../ML/vectorizer.pkl")


@app.route("/")
def home():
    return "AI Code Playground Backend Running"


@app.route("/predict", methods=["POST"])
def predict():

    data = request.get_json()

    code = data.get("code", "")

    code_vector = vectorizer.transform([code])

    prediction = model.predict(code_vector)[0]

    return jsonify({
        "prediction": prediction
    })


if __name__ == "__main__":
    app.run(debug=True)