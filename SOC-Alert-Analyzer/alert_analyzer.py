
# SOC Alert Analyzer
# Purpose: Identify open, high-severity malware alerts
# Data: Fictional security alerts for practice

# Step 1: Create security alerts
alerts = [
    {"id": "ALT-001", "type": "Malware", "severity": "High", "status": "Open"},
    {"id": "ALT-002", "type": "Phishing", "severity": "High", "status": "Open"},
    {"id": "ALT-003", "type": "Malware", "severity": "High", "status": "Open"},
    {"id": "ALT-004", "type": "Malware", "severity": "High", "status": "Closed"},
    {"id": "ALT-005", "type": "Malware", "severity": "High", "status": "Open"}
]

# Step 2: Count alerts requiring investigation
result = sum(
    alert["type"] == "Malware"
    and alert["severity"] == "High"
    and alert["status"] == "Open"
    for alert in alerts
)

# Step 3: Display the total
print("Open high-severity malware alerts:", result)

# Step 4: Display individual matching alerts
print("\nAlerts requiring investigation:")

for alert in alerts:
    if (
        alert["type"] == "Malware"
        and alert["severity"] == "High"
        and alert["status"] == "Open"
    ):

        print(
            f"Alert ID: {alert['id']} | "
            f"Type: {alert['type']} | "
            f"Severity: {alert['severity']} | "
            f"Status: {alert['status']}"
        )

# Step 5: Count alerts by type
print("\nSecurity Alert Summary:")

for alert_type in ["Malware", "Phishing", "Brute Force"]:
    count = sum(
        alert["type"] == alert_type
        for alert in alerts
    )
    print(f"{alert_type}: {count}")


# Step 6: Export matching alerts to CSV
import csv

with open("investigation_report.csv", "w", newline="") as file:
    writer = csv.DictWriter(
        file,
        fieldnames=["id", "type", "severity", "status"]
    )

    writer.writeheader()

    for alert in alerts:
        if (
            alert["type"] == "Malware"
            and alert["severity"] == "High"
            and alert["status"] == "Open"
        ):
            writer.writerow(alert)

print("\nInvestigation report saved successfully.")
