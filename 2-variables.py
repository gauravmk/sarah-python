print("Variables:\n---------")

# Part 1 - Variables
#
# Variables are used to store data like numbers, strings, lists, etc. Variables can have any name.
sarah = "Cool"
print(sarah) # Will print "Cool"

# You can reassign variables
sarah = "Awesome"
print(sarah) # Will print "Awesome"

# Assignment goes from right to left, so you can even do this
sarah = "So " + sarah
print(sarah) # What will this print?


# They can also store numbers
amount = 5
amount = amount + 1
print("Amount is:", amount) # What will this print?

# And lists
print("\nLists:\n------")

fruits = ["apple", "banana", "cherry"]

# You can access elements in a list using their index
print(fruits[0]) # Will print "apple"
print(fruits[1]) # Will print ??

fruits[1] = "orange"
print(fruits) # Will print ??

print(len(fruits)) # len returns the length of the list. Will print 3

# You can also add elements to a list
fruits.append("banana")
fruits.append("mango")
print(fruits) # Will print ???

# Variables can also store more complex data structures like dictionaries
print("\nDictionaries:\n------------")
sarah = {
    "name": "Sarah",
    "age": 35,
    "is_cute": True
}

print(sarah)
print("Her name is", sarah["name"])

sarah["age"] = 36
print("She is now", sarah["age"])

# Dictionaries can be nested, so these can be arbitrarily complex

movies = [
    {
        "title": "The Matrix",
        "cast": [{
            "name": "Keanu Reeves",
            "role": "Neo"
        }, {
            "name": "Laurence Fishburne",
            "role": "Morpheus"
        }],
        "year": 1999
    },
    {
        "title": "The Lord of the Rings",
        "cast": [{
            "name": "Elijah Wood",
            "role": "Frodo"
        }, {
            "name": "Ian McKellen",
            "role": "Gandalf"
        }],
        "year": 2001
    }
]
print(movies[0]["cast"][1]["name"]) # Will print "Laurence Fishburne"

# Task: Build a dictionary that captures the street address, city and state of our address.
print("\nTask:\n-----")
address = {} # TODO: Fill this in

# Now write a line of code that inserts the zip code into the address dictionary.

# Finally print out the city from the dictionary.