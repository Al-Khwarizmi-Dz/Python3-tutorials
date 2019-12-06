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
s = string[l - 1]
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
s = string[0:l]
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
s = string[0:l:2]
print(s)

# here the step is equal to 3
# this means taking the following
# 0, 3, 6, 9, ..., 24 <= 25
s = string[0:l:3]
print(s)

# printing the string in reverse
# here the step is equal to -1
# by going in reverse, 7, 6.....1
# in our our case it is form index 0, to index 25
# this means taking the following
# 25, 24, 23, 22, 21, ..., 0 <= 0
s = string[l::-1]
print(s)
