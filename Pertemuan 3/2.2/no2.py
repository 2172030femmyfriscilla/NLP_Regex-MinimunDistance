## All string that start at the beginning of the line with an integer and that end at the end of the line with a word
import re

# Pattern
pattern = r'^\d+\b.*\b([A-Za-z]+)$'

string = str(input("Insert String: "))

# Match test
match = re.match(pattern, string)

# Output
if (match):
    print(f"Found match: {match.group()}")
else:
    print("String not matched")