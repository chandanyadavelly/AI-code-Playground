from flask import Flask, request, jsonify
from flask_cors import CORS
import joblib

app = Flask(__name__)
CORS(app)

# Load ML files
model = joblib.load("../ML/model.pkl")
vectorizer = joblib.load("../ML/vectorizer.pkl")

def basic_syntax_check(code):

    # HTML tags
    html_tags = ["h1", "h2", "p", "div", "span", "button"]

    for tag in html_tags:
        if f"<{tag}>" in code and f"</{tag}>" not in code:
            return "error"

    # Parentheses
    if code.count("(") != code.count(")"):
        return "error"

    # Curly braces
    if code.count("{") != code.count("}"):
        return "error"

    # Square brackets
    if code.count("[") != code.count("]"):
        return "error"

    return None

@app.route("/")
def home():
    return "AI Code Playground Backend Running"


@app.route("/predict", methods=["POST"])
def predict():

    data = request.get_json()

    code = data.get("code", "")

    rule_result = basic_syntax_check(code)

    if rule_result:
        return jsonify({
            "prediction": rule_result
        })

    code_vector = vectorizer.transform([code])

    prediction = model.predict(code_vector)[0]

    return jsonify({
        "prediction": prediction
    })

if __name__ == "__main__":
    app.run(debug=True)