# split Returns a list where the string has been split at each match
import re

text = "apple,banana,orange,grape"
pattern = r","

split_result = re.split(pattern, text)
print("Split result:", split_result)