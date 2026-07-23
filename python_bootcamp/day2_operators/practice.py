a = 10
b = 20
print(a + b)

a = 10
b = 20
c = 30
print(a * b * c)

a = 10
b = 3
print(a % b)

a = 10
b = 3
print(a ** b)

minutes = int(input("Enter minutes: "))
hours = minutes / 60
print(f'{hours}hours')

a = 10
b = 20
a, b = b, a
print(a, b)

#area of rectangle

length = int(input("Enter a number: "))
breadth = int(input("Enter a number: "))
area = length * breadth
print(area)

# area of triangle
length = int(input("Enter a number: "))
breadth = int(input("Enter a number: "))
area = 0.5 *(length * breadth)
print(area)

# celcius to fahrenheit

celcius = float(input("Enter a number: "))
fahrenheit = (celcius * 9 / 5) + 32
print(fahrenheit)

a, b, c, d, e = 1, 2, 3, 4, 5
avg = (a + b + c + d + e ) / 5
print(avg)

# check if num is positive

num = int(input("Enter a number: "))
if num >= 0:
    print("num is positive")
else:
    print("num is negative")

#check if num is divisible by both 3 and 5
num = int(input("Enter a number: "))
if num % 3 == 0 and num % 5 ==0 :
    print("divisible by 3 and 5")
else:
    print("not divisible by 3 and 5")

#check a letter exits in your name
name = "bhanu"
print("a" in name)

# checking age is grater than or equal to 18

age = int(input("Enter your age: "))

if age >= 18:
    print("you are major")
else:
    print("you are not major")

#larger of two numbers
a = int(input("Enter a number: "))
b = int(input("Enter another number: "))
if a > b :
    print("a is greater than b")
elif a < b :
    print("a is less than b")
else:
    print("a is equal to b")


