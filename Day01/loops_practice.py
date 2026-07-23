for i in range(1,21):
    print(i)

for i in range(1,51):
    if i % 2 == 0:
        print(i)

for i in range(1,51):
    if i % 2 == 1:
        print(i)

total = 0
for i in range(1, 101):
    total += i
print(total)

for i in range (1, 11):
    print(f' 7 * {i} = {i * 7}')

nums = [45, 12, 78, 3, 90, 56]
largest = nums[0]
for num in nums:
    if num > largest:
        largest = num

print(largest)

nums = [45, 12, 78, 3, 90, 56]
smallest = nums[0]
for num in nums:
    if num < smallest:
        smallest = num

print(smallest)

nums = [45, 12, 78, 3, 90, 56]
total = 0
for num in nums:
    if num > 50:
        total += 1
print(total)

nums = [45, 12, 78, 3, 90, 56]
total = 0
for num in nums:
    if num % 2 == 0:
        total += num
print(total)

nums = [3, 8, 9, 12, 15, 20, 21]
total = 0
for num in nums:
    if num % 3 == 0:
        total += 1
print(total)

for i in range(5):
    for j in range(i+1):
        print("x" , end = "")
    print()

for i in range(5, 0, -1):
    for j in range(i):
        print("x" , end = "")
    print()


for i in range(5):
    for j in range(i+1):
        print( i  , end = "")
    print()

for i in range(1,5):
    for j in range(1, i+1):
        print( j  , end = "")
    print()

nums = [10, 20, 30, 40, 50]

rev = []

for i in range(len(nums)-1, -1, -1):
    rev.append(nums[i])
print(rev)

nums = [10, 25, 8, 99, 40]
largest = nums[0]
for i in nums:
    if nums[i] > largest:
        largest = nums[i]
print(largest)


