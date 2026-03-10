import joblib
import sys

# Load trained ML model
model = joblib.load("models/secure_lexer_model.pkl")
vectorizer = joblib.load("models/vectorizer.pkl")

print("\n🔍 Malicious Token Detection Engine Started\n")

if len(sys.argv) < 2:
    print("Usage: python detect_malicious_tokens.py <token_file>")
    exit()

token_file = sys.argv[1]

# create log file
log_file = open("logs/detection.log","w")

with open(token_file, "r") as f:
    tokens = [line.strip() for line in f if line.strip()]

X = vectorizer.transform(tokens)
predictions = model.predict(X)

for token, pred in zip(tokens, predictions):
    if pred == 1:
        message = f"MALICIOUS TOKEN: {token}"
    else:
        message = f"SAFE TOKEN: {token}"

    print(message)
    log_file.write(message + "\n")

log_file.close()
