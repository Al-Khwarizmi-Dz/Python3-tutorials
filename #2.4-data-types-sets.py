''' What is a set. '''
# it is a collection that holds, many objects in one place.
# the objects can have the same type, or it can also be diffrent.
# but the difference, is that the List can contain the same
# element more than once, but the Set can contain one copy, of
# each element only. (no duplications)

''' How to declare a set. '''
# fonction
lol = set()

# empty brackets
ll = {}

# with elements
# as you can see, The -lll- list holds many objects of different types.
# duplicates
lll = [1, False, 2, False, "Goal", "Goal"}

# no duplicates, it gives the same one
lll = {1, False, 2, "Goal"}

''' Lenght of a list. '''
# getting the lenght of the list
# len(lll) = 7
lenght = len(lll)

''' Mutability notion'''
# adding the refence
temp = lll

# adding a new element to temp, that is the same lll
temp.add(1997)

''' Slicing elemnts. '''
# when accessing the elemnts of the sets, we can not slice it,
# but only pop it. Because the sets can only access to the last element.

''' Accessing elemnts. '''
# it returns  the last element of the list, and delets it
element = lll.pop()

# to get the last element and not lose it
lll.add(element)

''' Some functions with the lists'''
# add a new elements
lll.add("New Element")
lll.add(123)

# delete an element
lll.remove(123)

# it returns  the last element of the list, and delets it
last = lll.pop()

# empty the list, delete all the elements
lll.clear()

# the intersection of the current set, with another.
# the intersection of two sets(A, B) is, a set that contains the
# the elements that exists in A and B, at the same time.
temp = {1, "Goal"}
inter = lll.intersection(temp)


# the intersection of the current set, with another.
# the intersection of two sets(A, B) is, a set that contains the
# the elements that exists in A and B, at the same time.
temp = {1, "Goal", 567, "Hi", 3.5}
inter = lll.intersection(temp)


# the union of the current set, with another.
# the union of two sets(A, B) is, a set that contains the
# the elements that exists in A adding to them, the elements that
# belongs to the set B, while taking in consideration the duplicates.
temp = {1, "Goal", 567, "Hi", 3.5}
union = lll.union(temp)


# chack id the current set, is a part(a subset) of the given set.
temp = {1, "Goal", 567, "Hi", 3.5}
temp1 = {1, "Goal"}
print(temp.issubset(lll))
print(temp1.issubset(lll))


'''
Please consider, veiwing the other functions on your own.
'''
