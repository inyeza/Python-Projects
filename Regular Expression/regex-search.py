# Search returns a Match object if there is a match anywhere in the string
import re

text = "The quick brown fox"
pattern = r"brown"

search = re.search(pattern, text)
if search:
    print("Pattern found:", search.group())
else:
    print("Pattern not found")