#Integers

#You can add (+), subtract (-), multiply (*), and divide (/) integers
a= 3872+89279
print(a) 
b= 938745-65134
print(b)
c= 153216*21653
print(c)
d= 16/4
print(d)
e= 10**5 # it means 10 power to the 5
print(e)

print(4+5*6)
print((4+5)*6) #be careful with paranthesis


#Floats

print(0.3+0.3)
print(3*0.7) # Be aware that you can sometimes get an arbitrary number of decimal places in your answer


# Avoiding Type Errors with the str() Function

#age=29
#message= " Happy " + age + "th Birthday!" #This is a type error
#print(message)  

age = 29
message = "Happy " + str(age) + "th Birthday!" 
# Do this by wrapping the variable in the str() function, which tells Python to represent non-string values as strings
print(message)

fav_number= 7
message = "My fav number is" + " " + str(fav_number)
print(message)
