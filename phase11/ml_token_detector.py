import joblib
import sys
import os

from threat_analyzer import analyze_token
from report_generator import generate_report

# require file input
if len(sys.argv) < 2:
    print("Usage: python3 ml_token_detector.py <file_path>")
    sys.exit(0)

file_path = sys.argv[1]

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

model_path = os.path.join(BASE_DIR, "models/secure_lexer_model.pkl")
vectorizer_path = os.path.join(BASE_DIR, "models/vectorizer.pkl")

model = joblib.load(model_path)
vectorizer = joblib.load(vectorizer_path)

# 🔥 READ FILE
with open(file_path, "r") as f:
    code = f.read()

# 🔥 TOKENIZE (simple)
import re
tokens = re.findall(r"[A-Za-z_]+|\d+", code)

threat_list = []
total_tokens = 0

for token in tokens:
    total_tokens += 1

    X = vectorizer.transform([token])
    prediction = model.predict(X)[0]

    if prediction == 1:
        category, severity = analyze_token(token)

        print(f"[{severity}] {token} -> {category}")

        threat_list.append({
            "token": token,
            "type": category,
            "severity": severity
        })

    else:
        print(f"[OK] {token}")

# 🔥 GENERATE FINAL REPORT (ONCE)
generate_report(file_path, threat_list, total_tokens)
