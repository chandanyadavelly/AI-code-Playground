import joblib

model = joblib.load("model.pkl")
vectorizer = joblib.load("vectorizer.pkl")

code = "<h1>Hello"

code_vector = vectorizer.transform([code])

prediction = model.predict(code_vector)

print("Prediction:", prediction[0])