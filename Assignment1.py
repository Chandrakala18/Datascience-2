#1.Basic String Manipulation:

#Assign the string "Hello, World!" to a variable and print it.
a="Hello,World!"
print(a)

#Create a string "Python Programming" and extract the first five characters using slicing.
a="Python Programming"
b=a[:5]
print(b)

#2.String Methods:

#Given a string "python is fun", convert it to uppercase.
a="python is fun"
print(a.upper())

#Replace "fun" with "awesome" in the string "Python is fun".
a="python is fun"
b=a.replace("fun","awesome")
print(b)
#3.String Formatting:

#Use f-string formatting to create a message like "My name is John, and I am 25 years old.", where the name and age are variables.
name="chandrakala"
age=25
print(f"My name is {name}, and I am {age} years old.")

#Given a price of 49.99, format it to display only two decimal places.
price = 49.99
a= (f"{price:.2f}")
print(a)

#4.String Functions:

#Count the occurrences of the letter 'o' in "Hello, how are you?"
a="Hello,how are you?"
b=(a.count("o"))
print(b)

#Find the position of "world" in "Hello, world! Python is amazing."
a="Hello, world python is amazing"
b=a.find("world")
print(b)

#4.Reverse and Check:

#Reverse the string "Python" using slicing.
a="python"
b=a[::-1]
print(b)

#Check if "madam" is a palindrome (a word that reads the same forward and backward). in python

a="madam"
b=a[::-1]
print(b)













