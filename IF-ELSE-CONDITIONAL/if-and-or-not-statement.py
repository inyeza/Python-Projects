#The and keyword is a logical operator, and is used to combine conditional statements:

#Example
#Test if a is greater than b, AND if c is greater than a:

a = 200
b = 33
c = 500
if a > b and c > a:
  print("Both conditions are True")

# The "or" keyword is a logical operator, and is used to combine conditional statements:
# Example
# Test if a is greater than b, OR if a is greater than c:

a = 200
b = 33
c = 500
if a > b or a > c:
  print("At least one of the conditions is True")

# The "not" keyword is a logical operator, and is used to reverse the result of the conditional statement:
# Example
# Test if a is NOT greater than b:

a = 33
b = 200
if not a > b:
  print("a is NOT greater than b")