import joblib
import sys
import os

# prevent crash if no token received
if len(sys.argv) < 2:
    sys.exit(0)

token = sys.argv[1]

# ignore symbols that break shell
ignore_tokens = ["(", ")", "{", "}", ";"]

if token in ignore_tokens:
    sys.exit(0)

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

model_path = os.path.join(BASE_DIR, "models/secure_lexer_model.pkl")
vectorizer_path = os.path.join(BASE_DIR, "models/vectorizer.pkl")

model = joblib.load(model_path)
vectorizer = joblib.load(vectorizer_path)

X = vectorizer.transform([token])
prediction = model.predict(X)[0]

if prediction == 1:
    print(f"[THREAT] Suspicious token detected -> {token}")
else:
    print(f"[OK] {token}")
