name = "bhanu"
print(name)
print(name[0])
print(name[-1])
print(len(name))
print(name.upper())
print(name.lower())
print(name.count("a"))
print(name.replace("a","@"))
print("h" in name )
print(name[1])
print(name[-3])

name = input("Enter your name: ")
print(name)
print(name[0])
print(name[-1])
print(len(name))
print(name.upper())
print(name.lower())
print(name.startswith("b"))
print(name.endswith("u"))
print(name[-1::])

for i in name:
    print(i)

vowels = 0
for char in name:
    if char in "aeiou":
        vowels += 1
print(vowels)