import re
import csv
from collections import Counter

# Read the file
with open("form.php", "r", encoding="utf-8") as file:
    content = file.read()

# Extract all emails (including duplicates)
emails = re.findall(r"[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.calldrip\.eu", content)

# Count occurrences of each unique email
email_counts = Counter(emails)

# Save to CSV with "Email" and "Count" columns
with open("unique_emails_with_count.csv", "w", newline="", encoding="utf-8") as output:
    writer = csv.writer(output)
    writer.writerow(["Email", "Count"])  # Header
    
    for email, count in email_counts.items():
        writer.writerow([email, count])

print(f"Extracted {len(email_counts)} unique emails and saved to unique_emails_with_count.csv")
