## All string that have both word 'grotto' and the word 'raven' in them (but not, e.g., words like 'grottos' that merely contain the word 'grotto')
import re

# Pattern
pattern = r'\b(?:grotto\b.*\braven|raven\b.*\bgrotto)\b'

string = str(input("Insert String: "))

# Match test
match = re.match(pattern, string)

# Output
if (match):
    print("String matched")
else:
    print("String not matched")