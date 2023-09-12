import re

text = "Hello, my email addresses are ikavin@skiff.com and immkavin.ofcl@gmail.com"

# Define a regular expression pattern for matching email addresses
pattern = r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,7}\b'

# Search for email addresses in the text
matches = re.findall(pattern, text)

for match in matches:
    print("Found:", match)
