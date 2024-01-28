# Python - Remove List Items
# 1. Remove specidied item: The remove() method removes the specified item

my_list = ["banana", "Apple", "Orange"]
my_list.remove("Apple")
print(my_list)

#N.B: If there are more than one item with the specified value, the remove() method removes the first occurance:
# Example
# Remove the first occurance of "banana":

thislist = ["apple", "banana", "cherry", "banana", "kiwi"]
thislist.remove("banana")
print(thislist)

#2. Remove Specified Index
#The pop() method removes the specified index.
# Example
# Remove the second item:

thislist = ["apple", "banana", "cherry"]
thislist.pop(1)
print(thislist)

#N.B: If you do not specify the index, the pop() method removes the last item.
# Example
# Remove the last item:

thislist = ["apple", "banana", "cherry"]
thislist.pop()
print(thislist)

# 3. The del keyword also removes the specified index:
# Example
# Remove the first item:

thislist = ["apple", "banana", "cherry"]
del thislist[0]
print(thislist)

# N.B: The del keyword can also delete the list completely.
# Example
# Delete the entire list:

thislist = ["apple", "banana", "cherry"]
del thislist

#4. Clear the List: The clear() method empties the list.
#The list still remains, but it has no content.
# Example
# Clear the list content:

thislist = ["apple", "banana", "cherry"]
thislist.clear()
print(thislist)