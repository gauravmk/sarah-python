# Loops let you run a block of code multiple times.

# The most basic loop is the while loop. It will run as long as the condition is true.
number = 1
while number < 10:
    print(number)
    number = number + 1
print("Done with the while loop")

# Here's asnother example handling a login
logged_in = True
while not logged_in:
    #password = input("What's the password? ")
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

number=3
while number != 1:
    if number % 2 == 0: #even
        number=(number/2)
    elif number % 2 != 0: #odd
        number=(number*3)+1
    print(number)
print("done!")

    #10 5 

# How would we print out each element in a list?
fruits = ["apple", "banana", "cherry", "dragonfruit", "eucalyptus", "frangipane"]
# Gaurav to implement with while loop, and then with a for loop
index = 0
while index<3: #bc only three in list
    print(fruits[index])
    index = index+1
print("done!")

#if we don't want to hardcode the value of index
index = 0
while index<len(fruits):
    #length of an array = len function
    print(fruits[index])
    index = index +1

#cleaner version
for fruit in fruits:
    print(fruit)


# Range is a function that returns a list of numbers from 0 to n-1
for number in range(1, 5):
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
# for element in array
#   do something with element

for movie_info in movies:
    print(movie_info["title"])
#want the variable to describe what it's holding to make the code easier to read

# Nested for loops!

# Building a times table
for i in range(1,6):
    for j in range(1,6):
        print(str(i) + "x" + str(j) + "=" + str(i * j))


for movie in movies:
    cast_array = movie["cast"]
    for cast_member in cast_array:
        print(cast_member["name"])
    
    # How would we print out the cast member name of each movie in the list?
for movie in movies: #movie is a type dictionary, movies is a type array
    for name in movie:
        print(cast)
