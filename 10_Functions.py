# FUNCTIONS

## Using a Function with a while Loop


# Defining a Function

def greet_user():
    print("Hello!")
greet_user()


## Passing Information to a Function

def visited_cities(city):  # city = parameter
    print("Hello, " + city.title() + "!")
visited_cities('istanbul') # argument

##try it yourself

def display_message():
    print("We are learning functions!")
display_message()

def favorite_book(title):
    print("One of my favorite books is " + title.title() + ".")
favorite_book('Alice in Wonderland')


# Passing Arguments

def visited_country(city_name,country_name):
    print("\nI have been in " + city_name + ".")
    print("The " + city_name.title() + " in " + country_name.title() + ".")
visited_country('naples', 'italy')


## Multiple Function Calls

def visited_country(city_name,country_name):
    print("\nI have been in " + city_name + ".")
    print("The " + city_name.title() + " in " + country_name.title() + ".")
visited_country('naples', 'italy')
visited_country('paris', 'france')


## Order Matters in Positional Arguments

def visited_country(city_name,country_name):
    print("\nI have been in " + city_name + ".")
    print("The " + city_name.title() + " in " + country_name.title() + ".")
visited_country('italy', 'naples') # so be careful!


# Keyword Arguments

def visited_country(city_name,country_name):
    print("\nI have been in " + city_name + ".")
    print("The " + city_name.title() + " in " + country_name.title() + ".")
visited_country(city_name = 'naples', country_name = 'italy') # be sure to use the exact names of the parameters in the function’s definition
visited_country(country_name = 'italy' , city_name = 'naples')


# Default Values
def fav_songs(song_name, singer_name = 'coldpaly'):
    print("My fav song is " + song_name + " by " + singer_name.title())
fav_songs('Something like this')


# Equivalent Function Calls

def visited_country(city_name,country_name):
    print("\nI have been in " + city_name + ".")
    print("The " + city_name.title() + " in " + country_name.title() + ".")
visited_country('naples', 'italy')

def make_shirt(message, size='large'):
    print(size + message)
make_shirt(message= 'I love Python')


# Return values
def get_pet(name, kind): 
	return name + ' ' + kind
username = get_pet('ruby', 'cat')
print(username)


def get_song(singer, song):
	return singer + song # it doesn't output the value 
	#print(singer + song) # it outputs the value
get_song('coldplay', ' viva la vida')

def get_formatted_name(first, last, middle = ''): 
	if middle: 
		full_name = first + ' ' + middle + ' ' + last 
	else: 
		full_name = first + ' ' + last 
	return full_name.title()

musician = get_formatted_name('kevser', 'rochdi', 'sila')
print(musician)


## Returning a Dictionary

def get_city(name, country): 
	trip = {'name': name, 'country': country} 
	return trip 
journey = get_city('Helsinki', 'Finland') 
print(journey)


## Using a Function with a while Loop

def get_formatted(name,lastname):
    full_name = name.title() + ' ' + lastname.title()
    return full_name

while True:
	first_name = input('type your first name: ') 
	last_name = input('type your last name: ') 
	fullname = get_formatted(first_name, last_name) 
	print(fullname) 





