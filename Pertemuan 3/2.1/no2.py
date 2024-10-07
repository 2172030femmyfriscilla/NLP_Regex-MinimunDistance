## The set of all lower case alphabetic string ending in a 'b'
import re

# Pattern
pattern = r'^[a-z]*b$'

string = str(input("Insert String: "))

# Match test
match = re.match(pattern, string)

# Output
if (match):
    print("String matched")
else:
    print("String not matched")