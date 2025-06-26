# Today's topics Functions, Lambda Expressions, and List Comprehensions

# Functions: Code reusability

def greet(name):
    return f"Hello {name}!"

print(greet("Avantika"))

def add(a, b):
    return a + b

print("Addition of 4 & 5 is: ", add(4,5))

def func1(name, hobby):
    return f"Name is {name} and hobby is {hobby}"

def func2(name , hobby ="none"):
    return f"Name is {name} and hobby is {hobby}"

print(func1("avantika","drawing")) #Positional argument
print(func1(hobby="Singing", name="sejal")) #Keywords argument
# print(func1("Saurabh"))  Error: Missing Positional argument
print(func2("saurabh")) #Default argument

# Lambda Functions: used inline without a name, returns the result of the expression, anonymous (unnamed) functions
 
square = lambda x: x * x
print(square(34))

mean = lambda x, y: (x+y)/2
print(mean(67, 54))

print((lambda s: s.upper())("hello!")) # inline lambda

#Use with map(), filter(), and reduce()

email =["avantikaj@gmail.com ", " Sejaljj@gmailcom", "SSJJ@outlook.com", "xyz.com"]
clean =list(map(lambda s: s.strip().lower(), email))
print(clean)

valid = list(filter(lambda s:s.find("@") != -1, clean))
print(valid)

from functools import reduce
num =[1, 3, 4, 7, 9]
total = reduce(lambda x, y: x + y, num)
print(total)