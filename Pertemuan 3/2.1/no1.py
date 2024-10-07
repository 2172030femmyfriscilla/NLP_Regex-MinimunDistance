## The set of all alphabetic string
import re

# Pattern
pattern = r'^[A-Za-z]+$'

string = str(input("Insert String: "))

# Match test
match = re.match(pattern, string)

# Output
if (match):
    print("String matched")
else:
    print("String not matched")