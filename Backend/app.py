from flask import Flask, request, jsonify
from flask_cors import CORS
import joblib
import google.generativeai as genai
import os

app = Flask(__name__)
CORS(app)

genai.configure(
    api_key=os.environ.get("GEMINI_API_KEY")
)

model_ai = genai.GenerativeModel("gemini-2.5-flash")

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

@app.route("/debug", methods=["POST"])
def debug_code():

    data = request.get_json()

    code = data.get("code", "")

    prompt = f"""
You are an expert programming debugger.

Analyze the following HTML, CSS and JavaScript code.

1. Identify errors.
2. Explain the issue clearly.
3. Suggest fixes.
4. Provide corrected code if needed.

Code:
{code}
"""

    response = model_ai.generate_content(prompt)

    return jsonify({
        "suggestion": response.text
    })


@app.route("/explain", methods=["POST"])
def explain_code():

    data = request.get_json()

    code = data.get("code", "")

    prompt = f"""
You are a programming tutor.

Explain the following code in simple language.

Requirements:
1. Explain what the code does.
2. Mention important HTML, CSS and JavaScript concepts used.
3. Keep the explanation beginner-friendly.

Code:
{code}
"""

    response = model_ai.generate_content(prompt)

    return jsonify({
        "explanation": response.text
    })


if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))
    app.run(host="0.0.0.0", port=port)