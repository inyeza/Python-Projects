# The strip() method removes any leading, and trailing whitespaces.
# Leading means at the beginning of the string, trailing means at the end.
# You can specify which character(s) to remove, if not, any whitespaces will be removed.

# Syntax = string.strip(characters) #with characters optional if we dont want to specify any character


# example1
txt = "     banana     "

x = txt.strip()

print("of all fruits", x, "is my favorite")

# example2
test = ",,,,,rrttgg.....banana....rrr"

x = test.strip(",.grt")

print(x)