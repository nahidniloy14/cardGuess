"""
FUNCTION
"""
"""
Functions allows us to create blocks of code that can be easily executed many times
without needing to rewrite the block of code
def name_of_function():
def is the keyword to identify this as a function
we use snake casing to write a function.
snake casing is all small letters with underscore between this to call a function we must use the paranthesis 
"""


#NON PARAMETERIZED
"""
def greet():
    print("Hello,Good Morning")
    print("Welcome To Dhaka")    
greet()

"""

#PARAMETERIZED
"""
def greet(name):
    print("Hello,Good Morning !!!")
    print(f"Welcome To Dhaka {name}")
greet("Niloy")
greet("John")
"""


#Using default value as a parameter
def greet(name):
    print(f'Hello!! good morning {name}')

greet('Abbas')

def greet(name='abcxyz'):
    print(f'Hello!! good morning {name}')

greet()

# Positional Argument
"""
def greet(f_name,l_name):
    print("Hello,Good Morning !!!")
    print(f"Welcome To Dhaka {f_name} {l_name}")
greet("Nahid Hassan","Niloy")

"""

# Keyword Argumet
def greet(f_name,l_name):
    print("Hello,Good Morning !!!")
    print(f"Welcome To Dhaka {f_name} {l_name}")

greet(f_name="Nahid Hassan",l_name="Niloy")


#return statement
def square(num):
    return num*num

print(square(2))



"""
Generate a string of random 8 numbers
"""
import random
import string

def generate_string():
    lettter_digits=string.ascii_letters+string.digits
    return ''.join(random.choice(lettter_digits) for i in range(8))

print(generate_string())

"""
Sum of series
"""
def sum_series(n,a,r):
    s=0
    for i in range(1,n+1):
        s+=a*(r**(i-1))

    return s
first_term=a=2
ratio=r=3
series=n=5

print(sum_series(n,a,r))