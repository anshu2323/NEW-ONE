

# Function is a collection of code which perform a specific task

def say_hi():                                    # keyword 'def' used to name a function followed by name():
      print("Hello User")                        # indentation is a must
      print("Today is 11 december 2021")         # indentation is a must
say_hi()

def say_hi(name,age):                            # Passing two parameters to function
    print("Hello " + name + " you are " + str(age) + " years old")
say_hi("anshu",28)
say_hi("punkoo",25)


# function which returns a value uses 'return' keyword

def cube(numb):
    return numb*numb*numb
print(cube(6))
print(cube(7))

# conditional statement if-else-elif with and/or conditions  :

# example 1
def check(i):
    if i==0 or i==5:                        # and keyword can also be used
        print("yes i = 0 or 5")
    elif i==10:
        print("ohh its 10")
    else:
        print("no i is not 0 or 5")
check(10)

# example 2 max_numb
def max_num(n1,n2,n3):
    if n1>n2 and n1>n3 :
        return n1
    elif n1<n3 :
        return n3
    else :
        return n2
print(str(max_num(40,70,10)) + " is the biggest")

# example 3 calculator
num1 = float(input("enter 1st number "))
op = input("enter the operator ")
num2 = float(input("enter the 2nd number "))
def calulator() :
    if(op=='+'):
        return num1+num2
    elif(op=='-'):
        return num1-num2
    elif(op=='*'):
        return num1*num2
    else:
        return num1/num2
print(calulator())



