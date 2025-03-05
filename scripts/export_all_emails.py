import re
import csv

# Read the file
with open("form.php", "r", encoding="utf-8") as file:
    content = file.read()

# Extract all emails (including duplicates)
emails = re.findall(r"[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.calldrip\.eu", content)

# Save to CSV with a "Number" column
with open("emails_with_numbers.csv", "w", newline="", encoding="utf-8") as output:
    writer = csv.writer(output)
    writer.writerow(["Number", "Email"])  # Header
    
    for i, email in enumerate(emails, start=1):
        writer.writerow([i, email])

print(f"Extracted {len(emails)} emails (including duplicates) and saved to emails_with_numbers.csv")
