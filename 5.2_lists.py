#Organizing a List

#Sorting a List Permanently with the sort() Method

colors= ['grey', 'green', 'purple', 'blue','black','white']
colors.sort() #store the list alphabetically
print(colors)

colors.sort(reverse=True) #reverse alphabetical order by passing the argument reverse=True to the sort() method
print(colors)


#Sorting a List Temporarily with the sorted() Function

colors= ['grey', 'green', 'purple', 'blue','black','white']
print("Here is my fave colors")
print(colors)
print("Here is sorted list?")
print(sorted(colors)) # lets you display your list in a particular order but doesn’t affect the actual order of the list
print("\n Here is original list again?")
print(colors)


#Printing a List in Reverse Order

my_fav_movies= ['Forrest Gump', 'Into the wild', 'Twilight']
print(my_fav_movies)

my_fav_movies.reverse() # To reverse the original order of a list.
print(my_fav_movies)


#Finding the Length of a List

my_fav_movies= ['Forrest Gump', 'Into the wild', 'Twilight']
n=len(my_fav_movies) #find the length of a list
print('I have',n, 'fav movies' )
print(len(my_fav_movies))


#Avoiding Index Errors When Working with Lists

#my_fav_movies= ['Forrest Gump', 'Into the wild', 'Twilight']
#print(my_fav_movies[3]) # index error: no item in my_fave_movies has an index of 3. Python starts indexing at 0!
#print(my_fav_movies[-2])