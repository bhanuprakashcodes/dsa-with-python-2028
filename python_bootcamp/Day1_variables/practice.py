name = "bhanu"
age = 20
cgpa = 7.2
branch = "cse"
print(name)
print(age)
print(cgpa)
print(branch)

name = input("Enter your name: ")
print(f'hello {name}')
print('welcome to python')

x = int(input("Enter a number: "))
y = int(input("Enter another number: "))

#Addition
result = x + y
print(result)

#Subtraction
result = x - y
print(result)

#Multiplication
result = x * y
print(result)

#Division
result = x / y
print(result)

birthyear = int(input("Enter your birth year: "))
age = int(input("Enter your age: "))

print(f'you are {age} years old')
print(f'your birthyear is {birthyear} ')

a = 10
b = 20

a, b = b, a
print(a)
print(b)

#Your favorite color is Blue

fav_colour = input("Enter your favorite colour: ")
print(f'your favorite colour is {fav_colour}')

a = float(input("Enter a number: "))
b = float(input("Enter another number: "))

c = a * b
print(c)

#Student: Bhanu
#Marks: 95
name = input("Enter your name: ")
marks = float(input("Enter your marks: "))
print(f'student{name}')
print(f'marks{marks}')

#radius of a circle

import math
radius = float(input("Enter your radius: "))
area = math.pi * radius ** 2
print(area)

#fullname

first_name = input("Enter your first name: ")
last_name = input("Enter your last name: ")
full_name = first_name + " " + last_name
print(full_name)