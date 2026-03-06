import os
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import classification_report, confusion_matrix, accuracy_score
import joblib

print("🚀 Week 8 - ML Training Started")

DATA_PATH = "datasets/lexical/tokens.csv"

if not os.path.exists(DATA_PATH):
    print("❌ tokens.csv not found. Run Week-7 pipeline first.")
    exit(1)

# Load dataset
df = pd.read_csv(
    DATA_PATH,
    names=["token", "type", "label", "line"],
    header=None
)

print("📊 Total samples:", len(df))

# Use only token column for feature extraction
X = df["token"]
y = df["label"]

# Split dataset
X_train, X_test, y_train, y_test = train_test_split(
    X, y,
    test_size=0.2,
    random_state=42,
    stratify=y
)

# TF-IDF vectorization
vectorizer = TfidfVectorizer(
    analyzer="char",   # character-level works better for tokens
    ngram_range=(1,3)
)

X_train_vec = vectorizer.fit_transform(X_train)
X_test_vec = vectorizer.transform(X_test)

# Logistic Regression classifier
model = LogisticRegression(
    max_iter=1000,
    class_weight="balanced"
)
model.fit(X_train_vec, y_train)

# Predictions
y_pred = model.predict(X_test_vec)

# Evaluation
print("\n📈 Accuracy:", accuracy_score(y_test, y_pred))
print("\n📋 Classification Report:\n")
print(classification_report(y_test, y_pred))
print("\n📊 Confusion Matrix:\n")
print(confusion_matrix(y_test, y_pred))

# Save model
os.makedirs("models", exist_ok=True)
joblib.dump(model, "models/secure_lexer_model.pkl")
joblib.dump(vectorizer, "models/vectorizer.pkl")

print("\n✅ Model saved to /models/")
