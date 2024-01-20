# In Python, a substring is a sequence of characters that is part of a string.
# For example, if we have the string “Hello World!”, some of its substrings are “Hello”, “World”, “lo W”, and so on

# example1
text = "Python is awesome"
substring = "is"
if substring in text:
    print(substring, "found in the text")

#example2
# Extracting a Substring from the Beginning
# In this example, we are trying to extract the starting word from the string.we used string slicing to extract the substring “Pytho” from the beginning of the string.
# The slice notation str[:5] starts at index 0 (the first character) and goes up to, but does not include, index 5, resulting in “Pytho”.
str = "Python is fun"
substring_start = str[:5]
print(substring_start)

#example2
# Extracting the Last Portion of the String
# In this example we are trying to extract the last portion of the string.
# we used string slicing to extract the substring “fun”.
# By omitting the end index, the slice extends to the end of the string, resulting in “fun”.

str1 = "Python is fun"
substring_end = str[10:]
print(substring_end)

# example3
# Extracting a Substring from the Middle
# In this example we are trying to extract the middle portion of the string.
# In this example, we specified both the start and end indices to extract the substring “is” from the text.
# The slice notation str[7:9] starts at index 7 and goes up to, but does not include, index 9, resulting in “is”.

str2 = "Python is fun"
substring_middle = str[7:9]
print(substring_middle)


