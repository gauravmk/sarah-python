# Conditionals allow you to specify code that only runs if a certain condition is met.

number = 5
if (number < 3):
    print("Number is less than 3")
elif (number >= 3 and number <= 10):
    print("Number is between 3 and 10")
else:    
    print("Number is greater than 10")

# Task: A user must be 21 or older to access a website.
birth_year = 2005
if (birth_year <=2004): # TODO: fill me in
    print("Welcome in!")
else:
    print("You are too young to enter.")


# Some basic comparison operators
5 > 3 # Greater than
5 == 3 # Equal to
5 != 3 # Not equal to
5 >= 3 # Greater than or equal to
5 <= 3 # Less than or equal to

# Things you can check with strings; each could be wrapped in an "IF" block
"apple" == "apple" # Equal to
"apple".startswith("app") # Starts with
"l" in "apple" # Contains

#an example with an list: does this list contain an element?
"apple" in ["apple", "banana", "cherry"] # Contains

# Movie Tasks!

movie_database = {
    "Titanic": {
        "director": "James Cameron", #string
        "actors": ["Leonardo DiCaprio", "Kate Winslet"], #list with square brackets
        "year": 1997
    },
    "Memento": {
        "director": "Christopher Nolan",
        "actors": ["Guy Pearce", "Carrie-Anne Moss"],
        "year": 2000
    },
    "The Prestige": {
        "director": "Christopher Nolan",
        "actors": ["Christian Bale", "Hugh Jackman"],
        "year": 2006
    },
    "Inception": {
        "director": "Christopher Nolan",
        "actors": ["Leonardo DiCaprio", "Joseph Gordon-Levitt"],
        "year": 2010
    },
    "Interstellar": {
        "director": "Christopher Nolan",
        "actors": ["Matthew McConaughey", "Anne Hathaway"],
        "year": 2014
    }
}

#movieName = "The Prestige" # For the tasks, make sure to change this to test different movies
#movieName = "Memento"
#movieName = "Titanic"
#movieName = "Inception"
movieName = "Interstellar"

movie = movie_database[movieName]

#print(movie["actors"])

# Task 1: I only like movies directed by Christopher Nolan from before 2010. 
# So create a conditional that says "I like this movie! It's got my favorite director" if the movie meets the criteria.

if (movie["director"]=="Christopher Nolan") and (movie["year"]<2010):
    print("I like this movie! It's got my favorite director!")
else:
    print("No director matches")


# Task 2: Actually, I like any movie that has either Leonardo DiCaprio or Christian Bale in it.
# Add a conditional that says "I like this movie! It's got my favorite actor" if the movie meets the criteria.

if "Leonardo DiCaprio" in movie["actors"] or "Christian Bale" in movie["actors"]:
    print("I like this movie! It's got my favorite actor!")
else:
    print("No actor matches")