import csv
import os

tokens_file = "datasets/lexical/tokens.csv"
report_file = "reports/security_report.txt"

threats = set()

# Read tokens dataset
if os.path.exists(tokens_file):
    with open(tokens_file, "r") as f:
        reader = csv.reader(f)
        for row in reader:
            if len(row) < 4:
                continue
            token, ttype, label, line = row

            if label == "1":
                threats.add((token, line))

# Write security report
with open(report_file, "w") as r:
    r.write("Security Analysis Report\n")
    r.write("========================\n\n")

    if not threats:
        r.write("No threats detected.\n")
    else:
        r.write("Detected Threats:\n")
        for token, line in sorted(threats):
            r.write(f"Token: {token} at line {line}\n")

print("Report generated at:", report_file)

# Clear dataset automatically for next run
open(tokens_file, "w").close()
print("Dataset cleared for next analysis.")
