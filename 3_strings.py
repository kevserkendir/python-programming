# Strings: Data Type

name= "marie"
print(name)


#Changing Case in a String with Methods

name= "Ada Lovelace"
print(name.title()) # this will change the value to capitalize format
print(name.upper()) # this will make it in uppercase
print(name.lower()) # that one will change the format to lowercase


#Combining or Concatenating Strings

first_name= "Kevser"
last_name= "Kendir"
full_name= first_name + " " + last_name
if we put " ". It executes like first_name + " " + last_name
print(full_name)
print("Hello, " + full_name.title() + "!")
message= "Hello, " + full_name.title() + "!"
print(message)


#Adding Whitespace to Strings with Tabs or Newlines

print("\tPython")
print("Python")

print("What we learn? : \nPython\nSQL\nMachine Learning") #with new line
print("What we learn? : \n\tPython\n\tSQL\n\tMachine Learning") #with new line and space


#Stripping Whitespace

singer="    Adele"
favsinger=singer.lstrip() # It removes the extra whitespace on the left side of a string.
print(favsinger)

singer="Adele      "
print(singer.rstrip())  # It removes the extra whitespace on the right side of a string.

singer="    Adele   "
print(singer.strip())  # It removes the extra whitespace on both sides.


#Avoiding Syntax Errors with Strings

fav_movie= 'Schindler's List' #do not use like this
fav_movie= "Schindler's List" #Avoide using apostrops inside a single quotes, it will cause errors. Use double quote!
print(fav_movie)
#let's try write a quote from steve jobs
print("Steve Job one said that: “Your time is limited, so don't waste it living someone else's life.”")

famous_person= "Steve Job one said that: “Your time is limited, so don't waste it living someone else's life.”"
print(famous_person)
