# A Simple Dictionary

from xml.etree.ElementPath import get_parent_map


my_fave_colors = {'1' : 'grey' , '2' : 'black'}
print(my_fave_colors['1'])
print(my_fave_colors['2'])


# Working with Dictionaries

## Accessing Values in a Dictionary

my_fave_colors = {'1' : 'grey' , '2' : 'black'}
new_color = my_fave_colors['2']
print("My fave color is " + str(new_color) + " ! ")


## Adding New Key-Value Pairs

my_fave_colors = {'1' : 'grey' , '2' : 'black'}
my_fave_colors['3']= 'khaki green' # Dictionaries are dynamic structures, and you can add new key-value pairs
print(my_fave_colors)


## Starting with an Empty Dictionary

my_fave_movies = {} # you can start empt dictionary and then add each new item to it.
my_fave_movies['1'] = 'the secret life of walter mitty'
my_fave_movies['2'] = 'into the wild'
print(my_fave_movies) 


## Modifying Values in a Dictionary

my_fave_movies = {'1': 'the secret life of walter mitty', '2': 'into the wild'}
print("My fave movie is " + my_fave_movies['1'] + " ! ") 
my_fave_movies['1'] = 'eat pray love' # To modify a value in a dictionary
print("My fave movie is now " + my_fave_movies['1'] + " !")


## Removing Key-Value Pairs

my_fave_movies = {'1': 'the secret life of walter mitty', '2': 'into the wild'}
print(my_fave_movies)

del my_fave_movies['2'] # Be aware that the deleted key-value pair is removed permanently.
print(my_fave_movies)


## A Dictionary of Similar Objects

fav_colors = {
    'kevser' : 'grey' ,
    'sila' : 'yellow' ,
    'rochdi' : 'purple' ,
}

print(" Sila's fav color is " + fav_colors['sila'].title() + "." )
fav_colors['sila']


# Looping Through a Dictionary

my_friends = {
    '1' : 'sila' ,
    '2' : 'rochdi' ,
    '3' : 'kerem' ,
    '4' : 'beth' ,
    '5' : 'aleren' ,
}

for number , name in my_friends.items():
    print("\nNumber: " + number )
    print("Name: " + name )
#for n , n1 in my_friends.items():
#print(my_friends)

for number , name in my_friends.items():
    print(name.title() + "'s fav color is blue ")


## Looping Through All the Keys in a Dictionary
''''
my_friends = {
    '1' : 'sila' ,
    '2' : 'rochdi' ,
    '3' : 'kerem' ,
    '4' : 'beth' ,
    '5' : 'aleren' ,
}
for name in my_friends.values():
    print(name.title())  # prints the names of everyone
my_fave_colors = {'1' : 'grey' , '2' : 'black'}
friends = [ 'kerem', 'sila']
for name in my_friends.values():
    print(name.title())

    if name in friends:
        print(" Hi " + name.title() + ", I see your fav color is " + my_fave_colors[name].title() + " ! ")

'''''
## Looping Through a Dictionary’s Keys in Order

favorite_languages = {
 'kevser': 'python',
 'sila': 'c',
 'rochdi': 'ruby',
 'kerem': 'python',
 }
for name in sorted(favorite_languages.keys()): #  use the sorted() function to get a copy of the keys in order.
    print(name.title() + ", thank you for your answers.")


## Looping Through All Values in a Dictionary

my_friends = {
    '1' : 'sila' ,
    '2' : 'rochdi' ,
    '3' : 'kerem' ,
    '4' : 'beth' ,
    '5' : 'aleren' ,
}
print("My fave people are: " )
for name in my_friends.values(): #you can use the values() method to return a list of values without any keys
    print(name.title())


# NESTING
'''
Sometimes you’ll want to store a set of dictionaries in a list or a list of 
items as a value in a dictionary. This is called nesting

'''

## A List of Dictionaries

friend_0 = { 'color' : 'red' , 'movie' : 'twilight'}
friend_1 = { 'color' : 'grey' , ' movie' : 'into the wild'}
friend_2 = { ' color' : ' blue' , 'movie' : 'skyfall'}

friends = [friend_0 , friend_1 , friend_2]
for friend in friends: 
    print(friend)

# Make an empty list for storing friends.
friends = []

# Make 10 fav friends
for friend_number in range(10):
    new_friend = {'color' : 'purple' , 'movie' : 'avatar'}
    friends.append(new_friend)

# Show the first 3 friends
for friend in friends[:3]:
    print(friend)
print("...")

# Show how many friends I have.
print("Total number of my fav friends: " + str(len(friends)))


## A List in a Dictionary

#Rather than putting a dictionary inside a list, it’s sometimes useful to put a list inside a dictionary
# Store information about the opened classes 

opened_class = {
    'oop' : 'object-oriented programming',
    'hci' : 'human computer interaction' ,
    'calculus' : ['filiz', 'ali'],

}

# Summarize the opened classes

print(" You can choose this lecturers :" +str(opened_class['calculus']) + " ! ") # use string not list!!
for calculus in opened_class['calculus']:
    print("\t" + calculus)


## A Dictionary in a Dictionary

users = {
    'crazygirl' : {
        'first' : 'sila',
        'last' : 'sur',
        'location' : 'istanbul'
    },
    'dangman' : {
        'first': 'rochdi',
        'last': 'khalid',
        'location' : 'casablanca',
    }
}
for username , user_info in users.items():
    print("\n Username : " + username)
    full_name = user_info['first'] + " " + user_info['last']
    location = user_info['location']

    print("\tFull name: " + full_name.title())
    print("\tLocation: " + location.title())


## Returning a Dictionary

def get_city(name, country): 
	trip = {'name': name, 'country': country} 
	return trip 
journey = get_city('Helsinki', 'Finland') 
print(journey)




