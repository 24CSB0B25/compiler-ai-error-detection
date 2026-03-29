import os
import json
import matplotlib.pyplot as plt

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
REPORTS_DIR = os.path.join(BASE_DIR, "reports")
GRAPH_DIR = os.path.join(BASE_DIR, "visualizations")

# ensure folder exists
os.makedirs(GRAPH_DIR, exist_ok=True)

files = []
scores = []

safe_scores = []
unsafe_scores = []

# 🔍 read reports
for file in os.listdir(REPORTS_DIR):
    if file.endswith("_report.json"):
        path = os.path.join(REPORTS_DIR, file)

        with open(path, "r") as f:
            data = json.load(f)

            # skip invalid files
            if "security_score" not in data:
                continue

            file_name = data["file"]
            score = data["security_score"]

            files.append(os.path.basename(file_name))
            scores.append(score)

            # classify
            if "safe" in file_name:
                safe_scores.append(score)
            elif "unsafe" in file_name:
                unsafe_scores.append(score)

# ❌ no data check
if not files:
    print("No valid data found!")
    exit()

# =========================
# 📊 GRAPH 1: FILE SCORES
# =========================
plt.figure()
plt.bar(files, scores)

plt.xticks(rotation=45)
plt.xlabel("Files")
plt.ylabel("Security Score")
plt.title("Security Analysis of Source Files")

plt.tight_layout()

file_graph_path = os.path.join(GRAPH_DIR, "security_scores.png")
plt.savefig(file_graph_path)

print(f"File-wise graph saved at: {file_graph_path}")

plt.close()


# =========================
# 📊 GRAPH 2: SAFE vs UNSAFE
# =========================
safe_avg = sum(safe_scores) / len(safe_scores) if safe_scores else 0
unsafe_avg = sum(unsafe_scores) / len(unsafe_scores) if unsafe_scores else 0

labels = ["Safe Files", "Unsafe Files"]
values = [safe_avg, unsafe_avg]

plt.figure()
plt.bar(labels, values)

plt.ylabel("Average Security Score")
plt.title("Safe vs Unsafe Code Comparison")

plt.tight_layout()

compare_graph_path = os.path.join(GRAPH_DIR, "safe_vs_unsafe.png")
plt.savefig(compare_graph_path)

print(f"Safe vs Unsafe graph saved at: {compare_graph_path}")

plt.close()

print("\n✅ Both graphs generated successfully!")
