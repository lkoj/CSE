"""
print("Hello World!")

# Apparently I'm going to slow, so i will speed up
# This is a comment
# THis has no effect on the code
# This is used for a variety of things, such as
# 1. Making personal notes about my code
# 2. Commenting out code that does not work

print("Notice what is happening Here.")
print()  # THis creates a new line
print()  # Do you notice the underline here?
#  Hover over top it to see what is wrong.



# Math
print(5 + 3)
print(5-3)
print(4 * 5)
print(6 / 5)
# semi-advance math
print(6 // 4)
print(12 // 3)
print(9 // 4)  # This give me a whole number
print()

print("Figure this out too...")
print(6 % 4)
print(5 % 3)
print(9 % 4)

# Defining Variables
car_name = "Wiebe mobile"  # String
car_type = "Tesla"  # String
car_cylinders = 16  # Integer
car_mile_per_gallons = 0.01  # Float

print("I have a car called %s. It's pretty nice." % car_name)
print("It has %d cylinders, but get %f mpg" % (car_cylinders, car_miles_per_gallon))



# Taking Input
name = input("what is your name? ")
print("Hello %s" % name)

age = input("How old are you?")
print("%s You belong in a museum!" % age)

# Recasting
real_age = input("How old are you again?")
hidden_age = real_age + 5
print(hidden_age)
"""

# Multi-Line Comments
"""
This is a multi-Line comment
anything in between them is automatically commented out.
"""


# Defining Function
def say_it():
    print("Hello World")


say_it()
say_it()
say_it()


# f(x) = 2x + 3
def f(x):
    print(2 * x + 3)


f(1)
f(5)
f(5000)


def distance(x1, y1, x2, y2):
    dist = ((x2 - x1) ** 2 + (y2 - y1) ** 2) ** (1 / 2)
    print(dist)


distance(0, 0, 3, 4)
distance(0, 0, 5, 12)

# For loops
for i in (1, 2, 3):
    say_it()

for i in range(5):  # Range (5) gives that numbers 0-4
    f(i)

for i in range(5):
    print(i ** 2)

# While loops
a = 0
while a < 10:
    print(a)
    a += 1  # This is the same as a = a + 1

"""
Hints for loops:
For loops - Use when you know EXACTLY how many iterations
While loops - Use when you DON'T know how many iterations
"""

# Control  Statements (If statements)
sunny = False
if sunny:
    print("Go outside")


def grade_calc(percentage):
    if percentage >= 90:
        return "A"
    elif percentage >= 80:
        return "B"
    elif percentage >= 70:
        return "C"
    elif percentage >= 60:
        return "D"
    else:
        return "F"


your_grade = grade_calc(82)
print(your_grade)

# Random numbers
import random  # This should be on line 1
print(random.randint(0, 100))

# Equality Statements
print(5 > 3)
print(5 >= 3)
print(3 == 3)
print(3 != 4)
"""
a = 3 # A is set to 3 
a == 3 # Is a equal to 3?
"""

# creating a list
fruit = ['apple', 'orange', 'blackberries', 'strawberries',
         'blueberries', "raspberries", "pineapple", "mango", "coconut"]  # Use Square Bracket
print(fruit)

# pulling items form a list
print(fruit[1])

# getting the length of a list
print(len(fruit))
print("The length of the list is %d" % len(fruit))

# Modifying Lists
fruit[8] = 'banana'
print(fruit)

# Looping through List
for item in fruit:
    print(item)

food_list = ["pizza", "tamales", "tacos", "pie", "enchiladas", "burrito",
             "sushi", "poke", "flan", "poutine", "noodles", "chicken",
             'chili', "Hot wings", "salmon", "chips", "lasagna", "soup"
             "fettuccine", "salad", "carne asada"]

# slicing
print(food_list[2:5])
print(food_list[3:4])
print(food_list[10:])
print(food_list[:5])

# Adding stuff to a list (part 1)
food_list.append("oranges")
food_list.append("bacon")
print(food_list)
# Everything is in the form Object.method(parameters)

# Adding to a list  (not at the end)
food_list.insert(2, "Goat")
print(food_list)

# Removing from a list
food_list.remove("tacos")
food_list.remove("pie")
print(food_list)
# This removes the specific item from the list

# Removing from a list (part 2)
# Sometimes, you don't know what is in the list, but
# You want to get rid of something at a specific
food_list.pop(0)
print(food_list)
# Notice that "pizza" is no longer in the because was is at index 0.

# practice item...

sport_list = ["Soccer", "football", "basketball"]

sport_list.append(4, "golf")

# Finding things in a list
print(food_list.index("chicken"))
# This printed 9 for me, so chicken must be at index 9.
# This is for an easy way of finding things in a list.

# Things I notice people do:
# Some people have made lists with parentheses instead of brackets
brand = ("apple", "samsung", "HTC")
# This is a TUPLE, not a list. Tuples are immutable ( cannot be changed)

# Changing things into a list
string1 = "turquoise"
list1 = list(string1)
print(list1)

for i in range(len(list1)):  # i goes through all indices
    if list1[i] == "u": # if we find a "u"
        list1.pop(i) # Remove the i-th index
        list1.index(i, "*")

# changing back into a string (list→string)
print("".join(list1))
