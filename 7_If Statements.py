# A Simple Example


from pickle import APPEND


cities= ['new york city','boston','san francisco','michigan']
for city in cities:
    if city == 'san francisco':
        print(city.upper())
    else:
        print(city.title())


# Conditional Tests

## Checking for Equality

city= 'san francisco'
city == 'san diego' # checks whether the value so we will get FALSE.
# This equality operator returns True if the values on the left and right side of the operator match, and False if they don’t match.

city= 'san francisco' #“Set the value of car equal to 'san francisco'.”
city == 'san diego' #“Is the value of car equal to 'san diego'?”


## Ignoring Case When Checking for Equality

city= 'san francisco'
city == 'San Francisco' #two values with different capitalization are not considered equal

city = 'San Francisco'
city.lower() == 'san francisco'
print(city)


## Checking for Inequality

ordered_food= 'lahmacun'
if ordered_food != 'kebap': # to determine whether two values are not equal
    print("It is also good idea for eating! :)")


# Numerical Comparisons

age=23 #do not use string value
age == 23
print(age)

result= 120 #string not compared 
if result == 120:
    print("Don't give up! Try one more time! :) ")

#include various mathematical comparisons
result= 120
result <121
result <= 121
print(result)


## Checking Multiple Conditions

### Using and to Check Multiple Conditions

result_0 = 98 
result_1=112 

result_0 >= 110 and result_1 >= 110 # we will get false because both side are not true
result_0 >=90 and result_1 >= 90 # we will get true because both side TRUE


### Using or to Check Multiple Conditions

result_0 = 98 
result_1=112
result_0 >= 110 and result_1 >= 110 #we will get TRUE.Because one of side is true.

result_0 = 98
result_1=112
result_0 >= 130 and result_1 >= 130 # we will get FALSE.Because both side false.


## Checking Whether a Value Is in a List

requested_languages = ['python','r','java','c++','javascript']
'python' in requested_languages # we will get TRUE.Because value in my list.
'sql' in requested_languages # we will get FALSE. Because it is not in the list.


## Checking Whether a Value Is Not in a List

visited_countries = ['turkey','italy','india','usa','jamaica']
country = 'morocco'

if country not in visited_countries:
    print("You can visit to " + country.title() + " whenever you want!")


## Boolean Expressions


# IF STATEMENTS

result = 108
if result >= 80:
    print( "Congratulations! You've passed the exam! ")
    print( "Let's start to paper work! ")


## IF-ELSE Statements

result= 95

if result >= 100:
    print("Congratulations! You've passed the exam! ")
    print( "Let's start to paper work! ")
else:
    print("Sorry, you haven't passed the exam.")
    print("Please, try again!")


## The IF-ELIF-ELSE Chain

age = 18

if age <= 25 :
    print(" Cost is $50 ")
elif age < 10 :
    print("Cost is $20")
else:
    print("Cost is $100 ")   

age = 18

if age <= 25 :
     Cost = 50
elif age < 10 :
    Cost = 20
else:
    Cost = 100  
 
print("Your admission cost is $" + str(Cost) + ".")


## Using Multiple elif Blocks

age = 18

if age <= 25 :
     Cost = 50
elif age < 10 :
    Cost = 20
elif age < 74 :
    Cost = 70
else:
    Cost = 100 
print("Your admission cost is $" + str(Cost) + ".")


## Omitting the else Block

age = 80

if age <= 25 :
     Cost = 50
elif age < 10 :
    Cost = 20
elif age < 74 :
    Cost = 70
elif age > 74 : # extra elif block is  clearer than the general else block.
    Cost = 30
print("Your admission cost is $" + str(Cost) + ".")


## Testing Multiple Conditions

visited_countries = ['turkey','italy','india','usa','jamaica']

if 'india' in visited_countries:
    print("One task is done!")
elif 'mexico' in visited_countries:
    print("You need a plan! ")
if 'canada' in visited_countries:
    print("One task is done!")
print("\n Take your time!You can visit more country. ")  


# Using if Statements with Lists

## Checking for Special Items

visited_countries = ['turkey','italy','india','usa','jamaica']

for visited_countries in visited_countries:
    print("I will visit " + visited_countries + " and many more.")
    if visited_countries == 'egypt':
        print("You should add your travel list. ")
    else:
        print(" Take your time.")


## Checking That a List Is Not Empty

opened_classes = []

if opened_classes:
    for opened_classes in opened_classes:
        print( "Adding " + opened_classes + ".")
    print("\ Did you finish select of classes?")
else:
    print(" Are you sure you want to graduate?? ")


## Using Multiple Lists

opened_classes = ['data structures', 'operation research','computer networks', 'human-computer interactions','algorithm and programming']
wanted_classes= ['data structures','human-computer interactions']

for wanted_classes in wanted_classes:
    if wanted_classes in opened_classes:
        print("Adding " + wanted_classes + " lectures.")
    else:
        print("Sorry , these classes " + wanted_classes + " will not opened this semestr.")



current_users=["sıla","kevser","rochdi","sevinç","aylin"]
new_users=["yusuf","sıla","ROCHDI"]
for i in new_users:
	if i in current_users:
		print("you need to enter a new username instead of"+ i)
	else:
		print("username is avaliable")


fruits = ['apple','kiwi','banana','watermelon','peach','strawberry','orange','blue berry']
my_fave_fruits = []
for my_fave_fruit in fruits:
    if my_fave_fruit == 'apple':
        my_fave_fruits.append('apple')
print(my_fave_fruits)
