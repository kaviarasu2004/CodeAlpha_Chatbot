"""
CodeAlpha - Task 3: Task Automation with Python Scripts
Automation idea chosen: Extract all email addresses from a .txt file
and save them to another file.
"""

import re
import os
import sys

EMAIL_PATTERN = r"[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}"


def extract_emails(input_file, output_file="extracted_emails.txt"):
    if not os.path.exists(input_file):
        print(f"Error: '{input_file}' not found.")
        return

    with open(input_file, "r", encoding="utf-8", errors="ignore") as f:
        content = f.read()

    emails_found = re.findall(EMAIL_PATTERN, content)
    unique_emails = sorted(set(emails_found))

    if not unique_emails:
        print("No email addresses found.")
        return

    with open(output_file, "w", encoding="utf-8") as f:
        for email in unique_emails:
            f.write(email + "\n")

    print(f"Found {len(unique_emails)} unique email address(es).")
    print(f"Saved to '{output_file}'.")
    for email in unique_emails:
        print(" -", email)


if __name__ == "__main__":
    if len(sys.argv) > 1:
        input_path = sys.argv[1]
    else:
        input_path = input(
            "Enter path to the .txt file to scan for emails: "
        ).strip()

    extract_emails(input_path)
