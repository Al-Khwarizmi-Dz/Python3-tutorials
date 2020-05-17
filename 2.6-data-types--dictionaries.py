''' What is a Dictionary. '''
# Dictionary in Python is an unordered collection of data values, used to
# store data values like a map, which unlike other Data Types that hold only
# single value as an element, Dictionary holds key:value pair. Key value is
# provided in the dictionary to make it more optimized.
# This tutorial is just an interpretation of this web site::
# (By https://www.geeksforgeeks.org/python-dictionary/)


''' How to declare a Dictionary. '''
# with a fonction
Dict = dict()

# With empty
Dict = {}

# with Integer Keys
Dict = {1: 'Geeks', 2: 'For', 3: 'Geeks'}

# with String Keys
Dict = {'1': 'Geeks', '2': 'For', '3': 'Geeks'}

# with Mixed keys
Dict = {'Name': 'Geeks', 1: [1, 2, 3, 4]}

# Creating a Nested Dictionary, a Dictionary inside another.
Dict = {1: 'Geeks', 2: 'For',
        3: {'A': 'Welcome', 'B': 'To', 'C': 'Geeks'}}

''' Lenght of a dictionary. '''
# getting the lenght of Dictionary, wich the number of the keys
lenght = len(Dict)

''' The Keys of a dictionary. '''
# getting the lenght of Dictionary, wich the number of the keys
keys = Dict.keys()

''' Manipulating elements. '''
# Accessing an alamant, Dict[key]
elem = Dict[1]

# Adding an element, Dict[key] = value
# adding one element, it can be any of the python data types
Dict[9] = 12  # integer
Dict[10] = "one"  # String
Dict[12] = ["Hello", True]  # list
Dict[13] = {"Hello", True}  # set
Dict[14] = ("Hello", True)  # tuple
Dict[15] = "Hello", True  # multiple values, at once
Dict[16] = {"False": False}  # dictionary

# Updating is the same at adding, but the key should already exists
# changing the element with the key 9, to a complex number.
# Dict[9] = 12 --> Dict[9] = (1 + 1j)
Dict[9] = (1 + 1j)

# deleting, del Dict[key]
del Dict[9]

''' Mutability notion'''
# adding the reference
temp = Dict

# adding a new (key, value)
# test the changes
temp["new-key"] = "temp"

''' Some functions with the lists'''
# get the list of all the dictionary keys
Dict.keys()

# get the element correspoding to the given key, and delete it with the key
# Dict.pop(key) --> returns the -value-
elem = Dict.pop(2)

# get the last element, and delete it
# Dict.popitem() --> returns the (key, value)
Dict.popitem()

# copy the dictionary
temp = Dict.copy()

# get the list of all the dictionary values
Dict.values()

# get the list of all the dictionary paires, (key, value)
Dict.items()

# access an element, Dict.get(key)
Dict.get(3)

'''
Please consider, veiwing the other functions on your own.
'''
