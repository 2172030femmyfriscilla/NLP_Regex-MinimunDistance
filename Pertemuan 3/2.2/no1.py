## The set of all string with two consecutive repeated words
import re

# Pattern
pattern = r'\b(\w+)\s+\1\b'

string = str(input("Insert String: "))

# Match test
match = re.match(pattern, string)

# Output
if (match):
    print(f"Found repeated word: {match.group()}")
else:
    print("String not matched")