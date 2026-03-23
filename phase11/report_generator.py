import json
import os

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
REPORTS_DIR = os.path.join(BASE_DIR, "reports")

def generate_report(file_name, threat_list, total_tokens):
    base_name = os.path.basename(file_name)
    name = os.path.splitext(base_name)[0]

    report_path = os.path.join(REPORTS_DIR, f"{name}_report.json")

    high = sum(1 for t in threat_list if t["severity"] == "HIGH")
    medium = sum(1 for t in threat_list if t["severity"] == "MEDIUM")
    low = sum(1 for t in threat_list if t["severity"] == "LOW")

    weighted = (high * 3) + (medium * 2) + (low * 1)

    score = max(0, int(100 - (weighted / total_tokens * 100))) if total_tokens > 0 else 100

    if score >= 80:
        risk = "LOW"
    elif score >= 50:
        risk = "MEDIUM"
    else:
        risk = "HIGH"

    report = {
        "file": file_name,
        "total_tokens": total_tokens,
        "threats": threat_list,
        "security_score": score,
        "risk_level": risk
    }

    with open(report_path, "w") as f:
        json.dump(report, f, indent=4)

    print("\n===== FINAL REPORT =====")
    print(f"File: {file_name}")
    print(f"Total Tokens: {total_tokens}")
    print(f"Threats: {len(threat_list)}")
    print(f"Security Score: {score}")
    print(f"Risk Level: {risk}")
