# A Match Object is an object containing information about the search and the result.
# Note: If there is no match, the value None will be returned, instead of the Match Object.
#Example
#Do a search that will return a Match Object:

import re

txt = "The rain in Spain"
x = re.search("ai", txt)
print(x) #this will print an object

#Example
#Print the position (start- and end-position) of the first match occurrence.

#The regular expression looks for any words that starts with an upper case "S":
#Search for an upper case "S" character in the beginning of a word, and print its position:
#import re

txt = "The rain in Spain"
x = re.search(r"\bS\w+", txt)
print(x.span())

# Example
# Print the string passed into the function:
#The string property returns the search string:

txt = "The rain in Spain"
x = re.search(r"\bS\w+", txt)
print(x.string)

#Example
#Print the part of the string where there was a match.
#The regular expression looks for any words that starts with an upper case "S" and print the word:

#import re

txt = "The rain in Spain"
x = re.search(r"\bS\w+", txt)
print(x.group())

#import re

text = "The quick brown fox"
pattern = r"quick"

match = re.match(pattern, text)
#print(match) # we can use thisone also
if match:
    print("Match found:", match.group())
else:
    print("No match")