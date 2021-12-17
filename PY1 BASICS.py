
# Strings are datatypes defined within quotes " or '
# Strings, int, float , boolean are primitive data structures.

print("Hello worlds")                               # prints hello world
a=int(input("enter a number"))                      # input takes a string as input so has to be typecasted to int for integer input
phrase="great"                                      # defining string variable
print(len(phrase),phrase.upper())                   # some functions
print(phrase[0])                                    #1st element of phrase
print(int(phrase.index('a')))                       # To find index of substring
print((phrase.replace("great","not so great")))     #To replace string with other string
print((phrase.find('at')))                          # To find a substring within a string
s="what a great day"
print(s.split())                                    # splits individual elements of the string

# NUMBERS

numb=5
print(str(numb) + " good number 5")                 #typecasting to string
number=5.5
num_2 = 4
print(abs(number))                                  # absolute value of number
print(pow(number,num_2))                            # power raise
print(max(number,num_2))                            # max of the two numbers
print(min(number,num_2))                            # min of the two numbers
print(round(number))                                # rounds the number

print(" CLASS 2 FOR SOME OTHER IMPORTANT MATH FUNCTIONS ")
from math import *                          # imports functions from math module
print(floor(number))                        # gives floor value
print(ceil(number))                         # gives ceiling value
print(sqrt(number))                         # gives square root of the number

print("class 3 some more cool stuff")
name = input("enter your name \n")             # input function
print(" Great game ", name)

print(" Lets play a madlibs game")             # matlibs game
number = input("enter a number :")
profession = input(" enter your profession :")
adj = input("enter the adjective")
print("you are " + number)
print("your profession is " + profession)
print("lets have some " + adj)




