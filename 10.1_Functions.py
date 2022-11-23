# PASSING A LIST

def fav_movies(movies):
    """ Print a simple movies to each movie in the list. """
    for movie in movies:
        msg = " Your fav movie: " + movie.title() + "!"
        print(msg)
movies = ['into the wild', 'forrest gump', 'city of god']
fav_movies(movies)


## Modifying a List in a Function

""" Any changes made to the list inside the function’s body are permanent"""
# Let's start with some unvisited countries.
unvisited_countries = ['germany', 'netherlands', 'belgium', 'portugal']
visited_countries = []

# Plan visiting countries, until none are left.
# Move each visited countries to visited_countries after visit it.
while unvisited_countries:
    current_situation = unvisited_countries.pop()

    #Plan you are visiting this countries.
    print("Visiting country: " +current_situation)
    visited_countries.append(current_situation)

# Display all visited countries.
    print("\nThe following countries have been visited:")
for visited_countries in visited_countries:
    print(visited_countries.title())

"""We can reorganize this code by writing two functions"""

def print_countries(unvisited_countries, visited_countries):
    """
    Make a plan to visiting each country, until none are left.
    Move to each country to visited_country after visited.
    """
    while unvisited_countries:
        current_situation = unvisited_countries.pop()

    #Make a plan to visit countries.
    print("Visiting country: " +current_situation)
    visited_countries.append(current_situation)

def show_visited_countries(visited_countries):
    """ Show all the countries that were visited."""
    print("\nThe following countries have been visited:")
    for visited_countries in visited_countries:
        print(visited_countries)

unvisited_countries = ['netherlands','iceland', 'poland','colombia']
visited_countries = []
print_countries(unvisited_countries, visited_countries)
show_visited_countries(visited_countries)


## Preventing a Function from Modifying a List


# Passing an Arbitrary Number of Arguments

def make_pizza(*toppings): # used to store multiple items in a single variable
 """Print the list of toppings that have been requested."""
print(toppings)
 
make_pizza('cheese')
make_pizza('red pepper', 'green peppers', 'extra cheese')

"""The asterisk in the parameter name *toppings tells Python to make an 
empty tuple called toppings and pack whatever values it receives into this 
tuple"""

def make_pizza(*toppings):
 """Summarize the pizza we are about to make."""
print("\nMaking a pizza with the following toppings:")
for topping in toppings:
        print("- " + topping)
 
make_pizza('margharita')
make_pizza('red pepper', 'green peppers', 'extra cheese')


## Mixing Positional and Arbitrary Arguments

def make_pizza(size, *toppings): 
 """Summarize the pizza we are about to make."""
print("\nMaking a " + str(size) +  # arbitrary number of arguments must be placed last in the function definition
 "-inch pizza with the following toppings:") 
for topping in toppings: 
    print("- " + topping) 
 
make_pizza(16, 'margharita') 
make_pizza(12, 'red pepper', 'green peppers', 'extra cheese')


## Using Arbitrary Keyword Arguments

def employee_profile(first, last, **user_info):
 """Build a dictionary containing everything we know about a user."""
profile = {}
profile['first_name'] = first
profile['last_name'] = last
for key, value in user_info():
    profile[key] = value
    return profile

user_profile = employee_profile('will', 'smith',
                                location = 'india',
                                field = 'ai')
print(user_profile)


# Storing Your Functions in Modules


## Importing an Entire Module

""" for example let's create visited_countries file with previous codes"""

import visited_countries



# Styling Functions

## Functions should has descriptive names wit lower cases
## Never forget to put comment that explains what function does.
## if you use 1 parameter, you do not need spaces but if you use more than 1 parameter put spaces. Let's look following example:
""" 
def function_name(parameter_0, parameter_1='default value')

def function_name(
 parameter_0, parameter_1, parameter_2,
 parameter_3, parameter_4, parameter_5):
 function body...
""" 