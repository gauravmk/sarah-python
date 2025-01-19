# Loops let you run a block of code multiple times.

# The most basic loop is the while loop. It will run as long as the condition is true.
number = 1
while number < 10:
    print(number)
    number = number + 1
print("Done with the while loop")

# Here's another example handling a login
logged_in = False
while not logged_in:
    password = input("What's the password? ")
    if password == "open sesame":
        logged_in = True
    else:
        print("Invalid password\n")
print("\nSuccessfully logged in")


# Task: Collatz Conjecture: https://en.wikipedia.org/wiki/Collatz_conjecture
# Given a number, the Collatz Conjecture states that you can always reach 1 if you follow these steps:
# If a number is even, divide it by 2
# If a number is odd, multiply it by 3 and add 1
# Repeat until you reach 1

initial_number = 3
# TODO: Implement the steps above printing out each number you get until you reach 1.
# For example, for the initial number 3, it should print out 3, 10, 5, 16, 8, 4, 2, 1



# How would we print out each element in a list?
fruits = ["apple", "banana", "cherry"]
# Gaurav to implement with while loop, and then with a for loop


# Range is a function that returns a list of numbers from 0 to n-1
for number in range(5):
    print(number)


# More movie tasks!

movies = [
    {
        "title": "The Matrix",
        "cast": [
            {"name": "Keanu Reeves", "role": "Neo"},
            {"name": "Laurence Fishburne", "role": "Morpheus"},
        ],
        "year": 1999,
    },
    {
        "title": "The Lord of the Rings",
        "cast": [
            {"name": "Elijah Wood", "role": "Frodo"},
            {"name": "Ian McKellen", "role": "Gandalf"},
        ],
        "year": 2001,
    },
]

# Task: Print out the name of each movie in the list


# Nested loops!

# Building a times table
for i in range(1,6):
    for j in range(1,6):
        print(i + "x" + j + "=" + i * j)

# How would we print out the cast of each movie in the list?