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
amount = amount + 1
print("Amount is:", amount) # What will this print?

# And lists
print("\nLists:\n------")

fruits = ["apple", "banana", "cherry"]
fruits2 = ["apple", "banana", "cherry", "pineapple", "pomegranate"]

# You can access elements in a list using their index []
print(fruits[0]) # Will print "apple"
print(fruits[1]) # Will print ??

fruits[1] = "orange"
print(fruits) # Will print ??

print(len(fruits)) # len returns the length of the list. Will print 3
print(len(fruits2))
# You can also add elements to a list using [listname].[append]
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

print(movies[1]["cast"][0]["role"]) # Will print

# Task: Build a dictionary that captures the street address, city and state of our address.
print("\nTask:\n-----")
address = {
    "street address": "139 Ashley Mews Dr",
    "city": "Ann Arbor",
    "state": "Michigan"
} # TODO: Fill this in


print(address["street address"] + ", " + address["city"] + ", " + address["state"])
# Now write a line of code that inserts the zip code into the address dictionary.

address["zip code"] = "48104"
print(address)

address["county"] = "washtenaw"
address["country"] = "USA"
print(address["county"],address["country"
                                ])
# Finally print out the city from the dictionary.
print(address["city"])