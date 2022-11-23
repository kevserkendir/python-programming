#Lists: square brackets ([]) indicate a list


songs= ['Hold Back the River by James Bay', 'Too Many Drugs by Rigoberta Bandini', 'Tu Me Dejaste De Quere by Nino de Elche', 'Preguntale al Polvo by Zahara']
print(songs)


#Accessing Elements in a List

songs= ['Hold Back the River by James Bay', 'Too Many Drugs by Rigoberta Bandini', 'Tu Me Dejaste De Quere by Nino de Elche', 'Preguntale al Polvo by Zahara']
print(songs[2]) # To access an element in a list. Starts from 0. 
print(songs[2].title()) # For capitalized all word.


#Index Positions Start at 0, Not 1

songs= ['Hold Back the River by James Bay', 'Too Many Drugs by Rigoberta Bandini', 'Tu Me Dejaste De Quere by Nino de Elche', 'Preguntale al Polvo by Zahara']
#Python considers the first item in a list to be at position 0, not position 1. 
print(songs[1]) # it access second song.
print(songs[3]) # it access forth song.
print(songs[-1]) #returns the last song in the list
print(songs[-3]) #returns the second song in the list


#Using Individual Values from a List

song= ['Hold Back the River by James Bay', 'Too Many Drugs by Rigoberta Bandini', 'Tu Me Dejaste De Quere by Nino de Elche', 'Preguntale al Polvo by Zahara']
message= "My fave song is " + song[1].title() + "." #concatenation to create a message based on a value from a list.
print(message)


#Changing, Adding, and Removing Elements

# Modifying Elements in a List

singer= ['Enrique Iglesias', 'Marc Antony', 'Rihanna', 'Teoman']
print(singer)

singer[2]='Imagine Dragons' #changes the value from Rihanna to Imagibe Dragons 
print(singer)


#Adding Elements to a List

singer= ['Enrique Iglesias', 'Marc Antony', 'Rihanna', 'Teoman']
print(singer)

singer.append('Hüsnü Arikan') #The append() method adds 'hüsnü arikan' to the end of the list without affecting any of the other elements in the list
print(singer)

#you can start with an empty list and then add items to the list using a series of append() statements.
singer=[]
singer.append('Coldplay')
singer.append('Adele')
singer.append('Teoman')
singer.append('Cem Karaca')
print(singer)


#Inserting Elements into a List

singer= ['Enrique Iglesias', 'Marc Antony', 'Rihanna', 'Teoman']
singer.insert(2, ' Coldplay' ) #now we added Coldplay as second element in list.
print(singer)
singer.insert(-1, ' Adele ' ) #it is not working use append instead of insert

#Removing Elements from a List

fav_series= ['La Casa De Papel', 'Merhamet', 'Anne with an e', 'Umutsuz Ev Kadinlari']
print(fav_series)

del fav_series[-1] # del to remove the last serie, 'umutsuz ev kadınları', from the list.
print(fav_series)

    #Removing an Item Using the pop() Method
fav_series= ['La Casa De Papel', 'Merhamet', 'Anne with an e', 'Umutsuz Ev Kadinlari']
popped_fav_series=fav_series.pop #pop() method removes the last item in a list, but it lets you work with that item after removing it.
print(fav_series)
print(popped_fav_series) 

fav_series= ['La Casa De Papel', 'Merhamet', 'Anne with an e', 'Bridgerton']
last_watched= fav_series.pop()
print("The last serie I watched was " + last_watched.title() + ".")

    #Popping Items from any Position in a List
fav_series= ['La Casa De Papel', 'Merhamet', 'Anne with an e', 'Bridgerton']
last_watched= fav_series.pop(0) # popping the first seri in the list, and then we print a message about that serie
print("The last serie I watched was " + last_watched.title() + ".")
#when you want to delete an item from a list and not use that item in any way, use the del statement; if you want to use an  item as you remove it, use the pop() method.

    #Removing an Item by Value
fav_series= ['La Casa De Papel', 'Merhamet', 'Anne with an e', 'Bridgerton']
print(fav_series)

fav_series.remove('Merhamet') #when you don't know the position of value but know the which value you want to delete it, then use remove() method.
print(fav_series)

fav_series= ['La Casa De Papel', 'Merhamet', 'Anne with an e', 'Bridgerton','Squid Game']
print(fav_series)
too_boring= 'Squid Game' # do not forget the define variable
fav_series.remove(too_boring) #the value has been removed from the list but is still stored in the variable too_boring
print(fav_series)
print("\nA " + too_boring.title() + " is too boring for me. Who want to continue such a this kinda serie?")

guests=['mother','father','sister','grandmother']
do_not=guests.pop()
new_attend=guests.append('kevser')
print(guests)

guests=['sila','rochdi', 'kevser']
popped_guests=guests.pop()
print(guests)
