"""####################################### Part-1 #######################################"""

'''
print, est une fonction pour afficher
print, is a function to display on the screen
print, هي فنكشن للعرض
'''

# declaration de la variable string
# declaration of the string variable with double quotation marks
string = "Fares is here."
print(string)

# declaration de la variable string1
# declaration of the string1 variable with double quotation marks
string1 = 'Fares is here.'
print(string1)

# in case we use the single quotation mark, in between
# a single quotaion string, we get an error.
# like this one:: 'I need help, i can't.'
shit = "I need help, i can't."
print(shit)

# in case we want to have a multi line python string
# we use """, instad of "
# or
string3 = """uhsdbfiugbsdiqufgsdqf
qsdfqsfqsfqsfsqdfsqfsqfsqfdsqfqs"""
print(string3)

# we use the ''', instad of '''
# don't worry of the usage, we'll get to that
string4 = '''uhsdbfiugbsdiqufgsdqf
qsdfqsfqsfqsfsqdfsqfsqfsqfdsqfqs'''
print(string4)

"""####################################### Part-2 #######################################"""
# believe it is not that complicated at all, i swear

string = "abcdefghijklmnopqrstuvwxyz"
# getting the lenght of our string
lol = len(string)
print(lol)

'''
Many ways to access the last element of your string
'''
# when visually knowing its lenght
s = string[25]
print(s)

# this one is general, you store the lenght into
# a variable, than you [l - 1] to index your last element
s = string[lol - 1]
print(s)

# this one is general and it is the best of all
# it works every time, it is one of the python bueaties
s = string[-1]
print(s)

'''
the sub strings, are a string but it is also a small
part of another string.
"abcde" is a sub string of "abcdefghijklmnopqrstuvwxyz"
i = the index of the first elemtn of the sub string
j = i + the lenght of your sub string
'''
# string = "abcdefghijklmnopqrstuvwxyz"
# sub_strign = "abcde"
# len(sub_string) = 5
# i = 0, becasue a have the index 0
# j = i + 5, j = 0 + 5, j = 5
# use [0: 5]
s = string[0:5]
print(s)

# string = "abcdefghijklmnopqrstuvwxyz"
# sub_strign = "ijk"
# len(sub_string) = 3
# i = 8, becasue a have the index 8
# j = i + 3, j = 8 + 3, j = 11
# use [8:11]
s = string[8:11]
print(s)

'''
printing the all string
'''
# the normal way, abvious
s = string[0:lol]
print(s)

# this means from the begining to the end of the string
s = string[:]
print(s)

'''
using steps, when sub-stringing(no idea if the term exists, but you
got the idea).
[i, j, step]:: going from i to j by jumping with step
i.e:: taking i, i + step, i + step + step, ..., i + step + step... + step <= j
'''
# here the step is equal to 2
# this means taking the following
# 0, 2, 4, 6, ..., 24 <= 25
s = string[0:lol:2]
print(s)

# here the step is equal to 3
# this means taking the following
# 0, 3, 6, 9, ..., 24 <= 25
s = string[0:lol:3]
print(s)

# printing the string in reverse
# here the step is equal to -1
# by going in reverse, 7, 6.....1
# in our our case it is form index 0, to index 25
# this means taking the following
# 25, 24, 23, 22, 21, ..., 0 <= 0
s = string[lol::-1]
print(s)

"""####################################### Part-3 #######################################"""

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

"""####################################### Part-4 #######################################"""

# variables
prenom = "Fares"
nom = "Herhar"
age = "22"

# concatinations des chaines
person = "Je suis " + prenom + " " + nom + ", et j'ai " + age + " ans."
print(person)

# formatting expression
person = "Je suis {} {}, et j'ai {} ans.".format(prenom, nom, age)
print(person)

# formatting expression with index
person = "Je suis {1} {0}, et j'ai {2} ans.".format(prenom, nom, age)
print(person)

# formatting expression with index maniupulation, and posisitions
country = "{0} is my country, {0} is {1}.".format("Algeria", "DZ")
print(country)

# a different syntax.
# both are correct.
country = "{0} is my country, {0} is {1}."
print(country.format("Algeria", "DZ"))
