from email_parser import parse_email
from detector import detect_phishing

email_data = parse_email("data/test_legitimate.eml")

result = detect_phishing(email_data)

print("\n========== EMAIL ==========")
print("From:", email_data["from"])
print("Subject:", email_data["subject"])

print("\n======= PHISHING ANALYSIS =======")
print("Risk:", result["risk"])
print("Score:", result["score"])

print("\nReasons:")

for reason in result["reasons"]:
    print("-", reason)
