## The set of all string from the alphabet 'a', 'b' such that each 'a' is immediately preceded by and immediately followed by a 'b'
import re

# Pattern
pattern = r'^(b(ab)*b*)*$'

string = str(input("Insert String: "))

# Match test
match = re.match(pattern, string)

# Output
if (match):
    print("String matched")
else:
    print("String not matched")