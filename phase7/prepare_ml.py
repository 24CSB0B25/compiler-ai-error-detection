import os
import pandas as pd
from sklearn.model_selection import train_test_split

print("🚀 Week-8 preparation started")

TOKENS = "datasets/lexical/tokens.csv"
MLDIR = "datasets/ml"

# check tokens file
if not os.path.exists(TOKENS):
    print("❌ tokens.csv not found")
    exit(1)

print("📂 Reading tokens.csv...")

df = pd.read_csv(
    TOKENS,
    names=["token","type","label","line"],
    header=None
)

print("📊 Rows loaded:", len(df))

if len(df) == 0:
    print("❌ Dataset empty")
    exit(1)

# clean
df = df.dropna().drop_duplicates()
print("📊 Rows after cleaning:", len(df))

# create ML folder
os.makedirs(MLDIR, exist_ok=True)

# split
train, test = train_test_split(
    df,
    test_size=0.2,
    random_state=42
)

train.to_csv(f"{MLDIR}/train.csv", index=False)
test.to_csv(f"{MLDIR}/test.csv", index=False)

print("✅ ML dataset ready")
print("   Train:", len(train))
print("   Test :", len(test))
