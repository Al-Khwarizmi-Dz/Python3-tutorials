''' What is a list. '''
# it is a collection that holds, manu object in one place.
# the objects can have the same type, or it can aldo be diffrent.

''' How to declare a list. '''
# fonction
lol = list()

# empty brackets
ll = []

# brackets, with elements
# as you can see, The -lll- list holds many objects of
# different types.
lll = [1, "string", [12], False, 1.23, (1 + 1j), True]

''' Lenght of a list. '''
# getting the lenght of the list
# len(lll) = 7
lenght = len(lll)

''' Accessing elemnts. '''
# first element
out = lll[0]

# second element
out = lll[1]

# last element
out = lll[-1]
out = lll[len(lll) - 1]

# before the last element
out = lll[-2]
out = lll[len(lll) - 2]

''' Mutability notion'''
# adding the refence
temp = lll

# adding a new element to temp, that is the same lll
temp.append(1997)

''' Slicing elemnts. '''
# copying the all the list
test = lll[:]  # method one
test = lll[0:]  # method two
test = lll[:len(lll)]  # method three
test = lll[0:len(lll)]  # method four

# copying the all the list, except the last element
# return to the [2.1.2-data-types-strings.py] file
test = lll[:-1]  # method one
test = lll[:len(lll) - 1]  # method two

# copying the list from, the first element to the third
# len(lll) = 7
# i = 0, becasue a have the index 0
# j = i + 3, j = 0 + 3, j = 3
# use [0:3]
test = lll[0:3]  # method one
test = lll[:3]  # method two

# copying the list from, the third element to the fifth
# len(lll) = 7
# i = 2, becasue a have the index 2
# j = i + 3, j = 2 + 3, j = 5
# use [2:5]
test = lll[2:5]

# copying the all the list, but the step is by 2
# so we'll be taking the index:: 0, 2, 4, 6 <= 6
# it can be any thing
test = lll[::2]

# copying the all the list, but the step is by 3
# so we'll be taking the index:: 0, 3, 6 <= 6
# it can be any thing
test = lll[::3]

# printing the string in reverse
# here the step is equal to -1
# by going in reverse, 9, 8, 7, 6.....1
# in our our case it is form index 0, to index 6
# this means taking the following
# 6, 5, 4, 3, 2, 1, 0 <= 0
temp = lll[l::-1]

''' Some functions with the lists'''
# add a new elements
lll.append("New Element")
lll.append(123)

# delete an element
lll.remove(123)

# get the index of an element
index = lll.index()

# indert a new element, at a spesific index
lll.insert("Element", 3)

# delete the last element of the list
lll.pop()

# empty the list, delete all the elements
lll.clear()


'''
Please consider, veiwing the other functions on your own.
'''
