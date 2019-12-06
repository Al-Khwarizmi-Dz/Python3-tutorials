# our string variable
string = 'azertyaatyytrty'

# the lenght of the variable
lenght = len(string)
print(lenght)

# converting an integer code to its
# corresponding caractere
# not sure, but i think that UTF-8 is the default encoding
ch = chr(100)
print(ch)

# the opposite of the previous functions
# it give the corresponding number(code)
# to a given caractere
num = ord('A')
print(num)

# make sure to not lose you original variable's
# values, because Strings are unmutable data types in python
# so, when a function(method) make a change to the string
# it doesn't do that localy but it creates a copy of it that makes
# the changes on, and returns it.
# string = string.capitalize()
ss = string.capitalize()
print(string)
print(ss)

# counting the number of the occurences
ss = string.count('a')
print(ss)

ss = string.count('aa')
print(ss)

# verifying if a string ends of starts with a another string
# even if it is a single caractere string
bll = string.endswith("rty")
print(bll)

bll = string.endswith("nnnnnn")
print(bll)

bll = string.startswith("aze")
print(bll)

# finding the a sub-string, and returning its first occurance index
num = string.find("rt")
print(num)

# returning its first occurance index
num = string.index("rt")
print(num)

# verifying if the string is digit
shit = "12345"
print(shit.isdigit())

# verifying if the string contains only alphabets
bll = string.isalpha()
print(bll)

# verifying if the string is all lower
bll = string.islower()
print(bll)

# verifying if the string is all upper
bll = string.isupper()
print(bll)

# converting all the string to upper
ss = string.upper()
print(ss)

# converting all the string to lower
sss = ss.lower()
print(sss)

# replacing a sub-string if it exists by another, and returns
# a new string with the modifications
new = string.replace("rt", "...")
print(new)
