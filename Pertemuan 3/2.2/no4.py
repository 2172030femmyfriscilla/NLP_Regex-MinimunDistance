## Write a pattern that places the first word of an English sentence in a register. Deal with punctuation
import re

# Pattern
pattern = r'^[^\w]*([A-Za-z]+)'

string = str(input("Insert String: "))

# Match test
match = re.match(pattern, string)

# Output
if (match):
    print(f"First word: {match.group(1)}")
else:
    print("No first word found")