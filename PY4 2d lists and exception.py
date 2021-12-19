# 2 d lists

number_grid = [                             # 2-d list
    [1,2,3,],
    [4,5,6],
    [7,8,9],
    [0]
]
print(number_grid)
print(number_grid[0][1])                # to print 2nd element of 1st list

# nested looping
for row in number_grid:
    for col in row:
        print(col)

# translator program which converts any vowel to g in the string
def translation(phrase):
    for letter in phrase:
        if letter in "AEIOUaeiou":
            letter='g'
            print(letter, end = ' ')
        else :
            print(letter, end=' ')
translation(input("enter a phrase "))

# another way to comment
''' These comments 
can be in 
multiple lines '''

try:
    i=int(input("enter a number"))
    print(i)
except ZeroDivisionError:
    print("divided by zero")
except ValueError:
    print("Invalid input")

