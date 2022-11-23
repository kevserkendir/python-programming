#Looping Through an Entire List

from traceback import print_tb
from turtle import title


names= ['kevser', 'sila','rochdi']
for name in names: #prints all names in a single name from names list.
    print(name.title()) 


#Doing More Work Within a for Loop

names= ['kevser', 'sila','rochdi']
for name in names: 
    print(name.title() + ", is an amazing person!")
    print("You will have an amazing life, " + name.title() + ".\n")
print("We are all great!")


#Avoiding Indentation Errors

#Forgetting to Indent

""""
names= ['kevser', 'sila','rochdi']
for name in names: 
print(name.title()) #IndentationError: expected an indented block after 'for' statement 
"""


#Forgetting to Indent Additional Lines

names= ['kevser', 'rochdi','sila']
for name in names: 
    print(name.title() + ", is an amazing person!")
print("I can't wait to see you again!, " + name.title() + ".\n") #s executed only once after the loop has finished running.
# this is logical error.


#Indenting Unnecessarily

message = "Hello Python world!"
print(message) #IndentationError: unexpected indent you don't need to indent print. There is no loop.


#Indenting Unnecessarily After the Loop

names= ['kevser', 'sila','rochdi']
for name in names: 
    print(name.title() + ", is an amazing person!")
    print("You will have an amazing life, " + name.title() + ".\n")
    print("We are all great!") #Python  will run all code that is written in valid syntax


#Forgetting the Colon

names= ['kevser', 'sila','rochdi']
for name in names: # do no froget the put colon ":".
    print(name.title())


#Making Numerical Lists

for value in range(1,7): # print a series of numbers 
   print(value)
 
for value in range(1,8): #o start counting at the first value you give it, and it stops when it reaches the second value
    print(value)


#Using range() to Make a List of Numbers

numbers= list(range(1,7)) #make a list of numbers
print(numbers)

even_numbers = list(range(2,11,2))  #list the even numbers
print(even_numbers)

odd_numbers = list(range(1,11,2))  #list the odd numbers
print(odd_numbers)

squares= []
for value in range (1,7):
    square= value**2
    squares.append(square)
print(squares)


#Simple Statistics with a List of Numbers

digits= [1,4,7,0,2,45,21,435,7]
min(digits)
max(digits)
sum(digits)
print(min(digits))
print(max(digits))
print(sum(digits))

#List Comprehensions

squares = [value**2 for value in range(1,11)] #uses a list comprehension
print(squares)


#Working with Part of a List

#Slicing a List

cities= ['san francisco', 'los angeles','new york city','chicago','florida']
print(cities[0:4]) # prints first four cities.
print(cities[:4]) # same with [0:4]
print(cities[1:4])
print(cities[2:]) #all items from the third item through the last item
print(cities[-2:]) # prints the last two cities


#Looping Through a Slice

cities= ['san francisco', 'los angeles','new york city','chicago','florida']
for city in cities[:3]:
    print(city.title())


#Copying a List

my_colours= ['grey','blue','green','black','white','purple','yellow','red']
friends_colours= my_colours[:4]

print("My fave colours are: ")
print(my_colours)

print("\n My friend fave colours are : ")
print(friends_colours)

my_colours.append('khaki green') # added new colour to my list
friends_colours.append('khaki green') # also don't forget the add friend's list.
print("My fave colours are: ")
print(my_colours)
print("\n My friend fave colours are : ")
print(friends_colours)


#TUPLES

#Defining a Tuple
#values that cannot change as immutable, and an immutable list is called a tuple.

numbers=(73,279)
print(numbers[0])
print(numbers[1])
#numbers[0]=97 # when we write this we will get error, because python can't assign a  new value to an item in a tuple


#Looping Through All Values in a Tuple

numbers=(73,279)
for number in numbers: # we might use for loop as well.
    print(number)


#Writing over a Tuple

numbers=(73,279)
print("Original numbers: ")
for number in numbers:
    print(number)

numbers=(3,576) # I got error
print("\n Modified numbers: ")
for number in numbers:
    print(number)

##PEP 8 style guide at https://python.org/dev/peps/pep-0008/