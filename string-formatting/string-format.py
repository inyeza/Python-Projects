#Example1
#Add a placeholder where you want to display the price:

price = 49
txt = "The price is {} dollars"
print(txt.format(price))

# Example2
# Format the price to be displayed as a number with two decimals:

price = 49
txt = "The price is {:.2f} dollars"
print(txt.format(price))

# Example3
# Multiple Values
# If you want to use more values, just add more values to the format() method:

quantity = 3
itemno = 567
price = 49
myorder = "I want {} pieces of item number {} for {:.2f} dollars."
print(myorder.format(quantity, itemno, price))

#Index Numbers
#You can use index numbers (a number inside the curly brackets {0}) to be sure the values are placed in the correct placeholders:
#Example4

quantity = 3
itemno = 567
price = 49
myorder = "I want {0} pieces of item number {1} for {2:.2f} dollars."
print(myorder.format(quantity, itemno, price))