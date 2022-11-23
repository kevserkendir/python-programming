# How the input() Function Works
'''
message = input("How was your day? : ") #pauses your program and waits for the user to enter some text
print(message)


## Writing Clear Prompts

name= input("Please write your fav song: ")
print("Wow, " +name + " is an amazing song.You have a good taste!")

prompt = "If you tell me what is your fav song is, I can know you better."
prompt += "\What is your fav song? "
song = input(prompt)
print("Wow, " +song + " is an amazing song.You have a good taste!")


## Using int() to Accept Numerical Input

age= input("How old do you feel you are?")
age = int(age) #int tells Python to treat the input as a numerical value.
age >= 23

score = input("What is your grade? ")
score = int(score)
if score >= 80:
    print("\nCongrats! You have been accepted!")
else:
    print("\nSorry, you have to take exam one more time.")


## The Modulo Operator

#modulo operator (%), which divides one number by another number and returns the remainder
number = input("Enter a number, and I'll tell you if it's even or odd: ")
number = int(number)
if number % 1 == 0:
 print("\nThe number " + str(number) + " is odd.")
else:
 print("\nThe number " + str(number) + " is even.")

### Ask the user for a number, and then report whether the number is a multiple of 10 or not.

number = input("Enter a number, and I'll tell you if it's multiple of 10 or not: ")
number = int(number)
if number % 10 == 0:
    print("\nThe number " + str(number) + " is multiple of 10! ")
else:
    print("\nThe number " +str(number) + " is not multiple of 10!")


# Introducing while Loops

current_visited = 5
while current_visited <= 10:
    print(current_visited)
    current_visited += 1
    

## Letting the User Choose When to Quit

prompt = "\nTell me something, and I will repeat it back to you:"
prompt += "\nEnter 'quit' to end the program. "
message = ""
while message != 'quit':
    message = input(prompt)
    print(message)

    if message != 'quit':
        print(message)


## Using a Flag

prompt = "\nTell me something, and I will repeat it back to you:"
prompt += "\nEnter 'quit' to end the program. "

'''

## Using break to Exit a Loop

prompt = "\nPlease enter the name of a city you have visited:"
prompt += "\n(Enter 'quit' when you are finished.) "

while True:
    city = input(prompt)

    if city =='finish': #  enter the names of cities you’ve been to until they enter 'quit'
        break #You can use the break statement in any of Python’s loops
    else: 
        print("My next destination is " + city.title() + "!")


## Using continue in a Loop

current_number = 5
while current_number < 43:
    current_number += 2
    if current_number % 3 == 0: #pass the number which divides to 3.
        continue #to return to the beginning of the loop based on the result of a conditional test
    print(current_number)


## Avoiding Infinite Loops

# This loop runs forever! use ctrl+c to stop running
x = 1
while x <= 6:
    print(x)
    x += 1 # ends the running forever 


#Using a while Loop with Lists and Dictionaries

## Moving Items from One List to Another

# start with cities that need to be verified
# and an empty list to hold visited cities.
unvisited_cities = ['berlin', 'amsterdam', 'prague']
visited_cities = []

# verified each city until there are no more unvisited cities.
# move each visited city into list of visited cities.
while unvisited_cities:
    visited_city = unvisited_cities.pop()

    print("Visited city: " + visited_city.title())
    visited_cities.append(visited_city)

# Display all visited cities.
print("\nThe following cities have been visited: ")
for visited_cities in visited_cities:
    print(visited_cities.title())
    

## Removing All Instances of Specific Values from a List

countries = ['germany', 'netherlands', 'germany','usa','italy']
print(countries)

while 'germany' in countries:
    countries.remove('germany') # remove the germany from list.
print(countries)


## Filling a Dictionary with User Input

responses = {}
# Set a flag to indicate that polling is active.
polling_active = True
while polling_active:
# Prompt for the person's name and response. 
    name = input("\nWhat is your name? ")
    response = input("Which city would you like to visit someday? ")

# Store the response in the dictionary:
responses[name] = response

# Find out if anyone else is going to take the poll.
repeat = input("Would you like to let another person respond? (yes/ no) ")
if repeat == 'no':
    polling_active = False

# Polling is complete. Show the results.
print("\n--- Poll Results ---")
for name, response in responses.items():
    print(name + " would like to visit " + response + ".")