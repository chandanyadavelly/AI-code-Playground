# AI-Powered Online Code Playground

## Project Overview

AI-Powered Online Code Playground is a full-stack web application that allows users to write, execute, test, analyze, and debug HTML, CSS, and JavaScript code in real time.

The project integrates Machine Learning and Generative AI to provide intelligent code analysis. A Naive Bayes model predicts whether the code contains errors, while Google's Gemini AI provides debugging suggestions and code explanations.

---

## Features

### Code Playground

* Write HTML, CSS, and JavaScript code
* Execute code instantly
* Live output preview
* Clear/Reset editor

### Machine Learning Module

* TF-IDF feature extraction
* Multinomial Naive Bayes classifier
* Predicts:

  * Error-Free Code
  * Code Contains Errors

### Rule-Based Syntax Validation

* HTML tag validation
* Parentheses validation
* Curly brace validation
* Square bracket validation

### Generative AI Module

* AI Debugging Assistant
* AI Error Explanation
* AI Fix Suggestions
* AI Code Explanation

### Additional Features

* Monaco Code Editor
* Professional UI Design
* Flask REST APIs
* GitHub Version Control

---

## Technology Stack

### Frontend

* HTML
* CSS
* JavaScript
* Monaco Editor

### Backend

* Python
* Flask
* Flask-CORS

### Machine Learning

* Scikit-Learn
* TF-IDF Vectorizer
* Multinomial Naive Bayes

### Generative AI

* Google Gemini API

### Tools

* Git
* GitHub
* VS Code

---

## Project Architecture

User Code Input
↓
Monaco Editor
↓
Run Code / Check Errors / Debug with AI / Explain Code
↓
Flask Backend
↓
Rule-Based Syntax Checker
↓
Naive Bayes ML Model
↓
Gemini AI
↓
Results Displayed to User

---

## Folder Structure

AI-Code-Playground/

├── Frontend/

│ ├── index.html

│ ├── style.css

│ └── script.js

│

├── Backend/

│ ├── app.py

│ ├── config.py

│ └── requirements.txt

│

├── ML/

│ ├── dataset.csv

│ ├── train_model.py

│ ├── test_model.py

│ ├── model.pkl

│ └── vectorizer.pkl

│

├── Documentation/

│

├── .gitignore

│

└── README.md

---

## Installation and Setup

### 1. Clone Repository

```bash
git clone https://github.com/chandanyadavelly/AI-code-Playground.git
cd AI-code-Playground
```

### 2. Create Virtual Environment

```bash
python -m venv venv
```

### 3. Activate Virtual Environment

Windows:

```bash
.\venv\Scripts\Activate.ps1
```

### 4. Install Dependencies

```bash
pip install flask flask-cors scikit-learn pandas numpy joblib requests google-generativeai
```

### 5. Configure Gemini API Key

Create:

```text
Backend/config.py
```

Add:

```python
GEMINI_API_KEY = "YOUR_API_KEY"
```

### 6. Start Backend

```bash
cd Backend
python app.py
```

### 7. Start Frontend

Open:

```text
Frontend/index.html
```

using Live Server.

---

## Machine Learning Workflow

1. Collect code samples
2. Label samples as:

   * error
   * no_error
3. Apply TF-IDF vectorization
4. Train Multinomial Naive Bayes model
5. Evaluate model
6. Save model using Joblib
7. Integrate with Flask API

---

## API Endpoints

### Home

```http
GET /
```

Response:

```text
AI Code Playground Backend Running
```

### Error Prediction

```http
POST /predict
```

Response:

```json
{
  "prediction": "error"
}
```

### AI Debugging

```http
POST /debug
```

Response:

```json
{
  "suggestion": "AI debugging suggestion..."
}
```

### AI Code Explanation

```http
POST /explain
```

Response:

```json
{
  "explanation": "AI code explanation..."
}
```

---

## Future Enhancements

* Multi-language support
* User authentication
* Cloud deployment
* Project saving feature
* Dark mode
* AI code optimization
* Collaborative coding

---

## Author

Yedavalli Chandan Kumar - 237R1A66C5

B.Tech Final Year Student

Department of CSE (AI & ML)

CMR Technical Campus

---

## License

This project is developed for academic and educational purposes.
