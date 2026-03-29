import os
import json

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
REPORTS_DIR = os.path.join(BASE_DIR, "reports")
reports = []

for file in os.listdir(REPORTS_DIR):
    if file.endswith("_report.json"):
        path = os.path.join(REPORTS_DIR, file)

        with open(path, "r") as f:
            data = json.load(f)

            # 🔥 FIX: skip invalid reports
            if "security_score" not in data:
                continue

            reports.append(data)

# ❌ Handle empty case
if not reports:
    print("No valid reports found!")
    exit()

# 🔥 Sort by score
reports_sorted = sorted(reports, key=lambda x: x["security_score"], reverse=True)

# 📊 Compute summary
total_files = len(reports)
avg_score = sum(r["security_score"] for r in reports) / total_files

best = reports_sorted[0]
worst = reports_sorted[-1]

summary = {
    "files_analyzed": total_files,
    "average_score": round(avg_score, 2),
    "most_secure_file": best["file"],
    "most_secure_score": best["security_score"],
    "least_secure_file": worst["file"],
    "least_secure_score": worst["security_score"]
}

# 💾 Save summary
summary_path = os.path.join(REPORTS_DIR, "summary_report.json")

with open(summary_path, "w") as f:
    json.dump(summary, f, indent=4)

# 🖥️ Print results
print("\n===== COMPARATIVE ANALYSIS =====")
print(f"Files analyzed: {total_files}")
print(f"Average score: {avg_score:.2f}")
print(f"Best file: {best['file']} ({best['security_score']})")
print(f"Worst file: {worst['file']} ({worst['security_score']})")
