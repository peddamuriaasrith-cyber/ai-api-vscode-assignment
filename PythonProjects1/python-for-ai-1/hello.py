print("Hello World")

age = 25
has_license = True

# AND - both must be true
can_drive = age >= 16 and has_license
print(can_drive)  # True

first_name = "Jane"
last_name = "Doe"

# Using +
full_name = first_name + " " + last_name  # "Jane Doe"
print(full_name)  # Jane Doe


age = 15

if age >= 18:
    print("You can vote!")
    print("You're an adult")

else:
    print("You cannot vote yet.")
    print("You're a minor!")

    score = 90

if score >= 90:
    print("A - Excellent!")
elif score >= 80:
    print("B - Good job!")
elif score >= 70:
    print("C - Keep it up!")
else:
    print("F - Need improvement")

for i in range(4):
    print("Hello World")


my_list = []

fruits = ["apple", "banana", "orange"]
numbers = [1, 2, 3, 4, 5]
mixed = ["hello", 42, True, 3.14]  # Different types OK!

# Get items
print(fruits[0])    # "apple" (first item)
print(fruits[1])    # "banana"
print(fruits[-1])   # "orange" (last item)
print(fruits[-2])   # "banana" (second to last)

# Slicing
print(fruits[0:1]) # ["apple"]
print(fruits[1:2])   # ["banana"]


def greet():
    print("Hello, world!")
    print("Welcome to Python!")

# Call the function
greet()


def check_weather():
    temperature = 25
    if temperature > 30:
        print("It's hot!")
    else:
        print("Nice weather!")

# Use the function
check_weather()