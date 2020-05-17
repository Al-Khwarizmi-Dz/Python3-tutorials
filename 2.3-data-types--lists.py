''' What is a list. '''
# it is a collection that holds, many objects in one place.
# the objects can have the same type, or it can also be diffrent.

''' How to declare a list. '''
# fonction
lol = list()

# empty brackets
ll = []

# brackets, with elements
# as you can see, The -lol- list holds many objects of
# different types.
lol = [1, "string", [12], False, 1.23, (1 + 1j), True]

''' Lenght of a list. '''
# getting the lenght of the list
# len(lol) = 7
lenght = len(lol)

''' Accessing elemnts. '''
# index = position - 1
# first element
out = lol[0]

# second element
out = lol[1]

# last element
out = lol[-1]
out = lol[len(lol) - 1]

# before the last element
out = lol[-2]
out = lol[len(lol) - 2]

''' Mutability notion'''
# adding the refence
temp = lol

# adding a new element to temp, that is the same lol
temp.append(1997)

''' Slicing elemnts. '''
# copying the all the list
test = lol[:]  # method one
test = lol[0:]  # method two
test = lol[:len(lol)]  # method three
test = lol[0:len(lol)]  # method four

# copying the all the list, except the last element
# return to the [2.1.2-data-types-strings.py] file
test = lol[:-1]  # method one
test = lol[:len(lol) - 1]  # method two

# copying the list from, the first element to the third
# len(lol) = 7
# i = 0, becasue a have the index 0
# j = i + 3, j = 0 + 3, j = 3
# use [0:3]
test = lol[0:3]  # method one
test = lol[:3]  # method two

# copying the list from, the third element to the fifth
# len(lol) = 7
# i = 2, becasue a have the index 2
# j = 5, because it is the fifth element
# use [2:5]
test = lol[2:5]

# copying the all the list, but the step is by 2
# so we'll be taking the index:: 0, 2, 4, 6 <= 6
# it can be any thing
test = lol[::2]

# copying the all the list, but the step is by 3
# so we'll be taking the index:: 0, 3, 6 <= 6
# it can be any thing
test = lol[::3]

# printing the string in reverse
# here the step is equal to -1
# by going in reverse, 9, 8, 7, 6.....1
# in our our case it is form index 0, to index 6
# this means taking the following
# 6, 5, 4, 3, 2, 1, 0 <= 0
test = lol[len(lol)::-1]

''' Some functions with the lists'''
# add a new elements
lol.append("New Element")
lol.append(123)

# delete an element
lol.remove(123)

# get the index of an element
index = lol.index()

# indert a new element, at a spesific index
lol.insert("Element", 3)

# it returns  the last element of the list, and delets it
last = lol.pop()

# empty the list, delete all the elements
lol.clear()

''' Extra '''
one = [1, 2, 3]
two = [4, 5, 6]
temp = one + two

'''
Please consider, veiwing the other functions on your own.
'''
