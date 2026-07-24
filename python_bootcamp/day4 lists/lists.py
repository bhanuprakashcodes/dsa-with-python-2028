fruits = ["apple", "banana", "coconut", "orange", "strawberry"]
print(fruits)
print(fruits[0])
print(fruits[-1])
print(len(fruits))
fruits[3] = "mango"
print(fruits)
fruits.append("pineapple")
print(fruits)
fruits.insert(2, "kiwi")
print(fruits)
fruits.remove("banana")
print(fruits)
fruits.pop()
print(fruits)

numbers = [45, 12, 89, 23, 67]
print(89 in numbers)
for num in numbers:
    print(num)

largest = numbers[0]
for num in numbers:
    if num > largest:
        largest = num
print(largest)

smallest = numbers[0]
for num in numbers:
    if num <smallest:
        smallest = num
print(smallest)

total = 0
for num in numbers:
    total += num
print(total)


numbers = [45, 12, 89, 23, 67]
total = 0
for num in numbers:
    total += num
average = total / len(numbers)
print(average)

count = 0
for num in numbers:
    if num % 2 == 0:
        count += 1
print(count)


count = 0
for num in numbers:
    if num % 2 == 1:
        count += 1
print(count)

nums = []
for num in numbers:
    if num > 30:
        nums.append(num)
print(nums)

nums = []
for num in numbers:
    if num < 50:
        nums.append(num)
print(nums)

largest = numbers[0]
for num in numbers:
    if num > largest:
        largest = num
        numbers.remove(largest)
secondlargest = numbers[0]
for num in numbers:
    if num > secondlargest:
        secondlargest = num
print(secondlargest)