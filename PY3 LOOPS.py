
# While loop
i=1
while i<5:
    print(i)
    i=i+1                                       # prints i=1 till 5

# For Loop example 1 use in strings
for letter in "Won":
    print(letter)

# example 2 use in lists/arrays
friends=["jim","karen","mathew"]
for friend in friends:
    print(friend)

# example 3 use in ints, here range is a keyword function
for num in range(3,10):                     # RANGE FUNCTIONS OUTPUTS AN ORDERED SEQUENCE AS  A LIST 'i'
    print(num)                              # range(start,stop,step)
list(range(1,10,2))                         # prints 1,3,5,7,9
# exponent function
print(2**4)                                 # two ** is for power, exponent
def exponent(base,power):
    i=1
    x=base
    while i<power:
        x=x*base
        i=i+1
    return x
print(exponent(5,4))

    
