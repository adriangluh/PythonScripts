import re

# Read the file
with open("form.php", "r", encoding="utf-8") as file:
    content = file.read()

# Extract emails
emails = set(re.findall(r"[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.calldrip\.eu", content))

# Save to CSV
with open("emails.csv", "w", encoding="utf-8") as output:
    output.write("Email\n")  # Header
    output.write("\n".join(sorted(emails)))

print(f"Extracted {len(emails)} unique emails and saved to emails.csv")
