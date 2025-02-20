# for loop in python
#

fruits = ["apple", "banana", "cherry"]

for fruit in fruits:
    if fruit == "banana":
        print("Banana is my favorite fruit")
    else:
        print(f"{fruit} not my favorite fruit")

# while

count = 0

while count < 5:
    print(count)
    count += 1

# for loop with range

for index, fruit in enumerate(fruits):
    print(index, fruit)

# for loop with break

for fruit in fruits:
    if fruit == "banana":
        break
    print(fruit)

# for loop with continue

for fruit in fruits:
    if fruit == "banana":
        continue
    print(fruit)

# for loop with else

for fruit in fruits:
    print(fruit)
else:
    print("Finally finished!")

# for with zip

names = ["John", "Peter", "Vicky"]
ages = [23, 45, 34]

for name, age in zip(names, ages):
    print(f"{name} is {age} years old")
