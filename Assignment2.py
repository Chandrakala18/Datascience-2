#1.Even or Odd Checker Write a Python program that takes an integer input from the user and determines whether the number is even or odd using an if-else statement.
'''n=int(input("Enter the number"))
if(n%2==0):
    print("even")
else:
    print("odd")   
'''

#2.Find the Largest Number Create a Python program that takes three numbers as input and uses if-else conditions to find and display the largest number.     
'''a=int(input("Enter first number"))
b=int(input("Enter second number"))
c=int(input("Enter third number"))
if(a>b and a>c):
    print("The largest number is:",a)
elif(b>a and b>c):
    print("The largest number is:",b)  
else:
    print("The largest number is:",c)   
'''
#3.Number Classification Write a program that takes a number input and checks if the number is positive, negative, or zero using if-elif-else conditions.
'''n=int(input("enter a number"))
if(n>0):
    print("positive")
elif(n<0):
    print("negative")
else:
    print("Zero")        
'''
 #4.Sum of Numbers in a Range Write a Python program that takes two numbers (start and end) as input and uses a for loop to compute and display the sum of all numbers in that range   
'''start=int(input("Enter start number: "))
end=int(input("Enter end number: "))
sum=0
for i in range(start, end + 1):
    sum=sum+i
print(sum)
'''
#5.Printing a Multiplication Table Develop a Python program that takes an integer as input and prints its multiplication table from 1 to 10 using a for loop.
'''n=int(input("Enter a number:"))
for i in range(1,11):
    print(n,"*",i,"=",n*i)'
'''
#6.Counting Vowels in a String Write a Python script that takes a string input from the user and uses a for loop to count the number of vowels (a, e, i, o, u) present in the string.
'''a=input("Enter a string:")
vowels="aeiou"
c=0
for i in a:
    if i in vowels:
        c=c+1
print(c)        
'''
#7.Factorial Calculator Create a Python program that takes a positive integer as input and calculates its factorial using a for loop.
'''n=int(input("Enter a number"))
if(n<0):
    print("Factorial is not defined for negative number")
else:
    f=1
    for i in range(1,n+1):
        f=f*i
    print(f"The factorial of {n} is {f}")        
'''
#8.FizzBuzz Game Write a Python program that prints numbers from 1 to 50. 
'''for i in range(1,51):
    if(i%3==0 and i%5==0):
        print("FizzBuzz")
    elif(i%3==0):
        print("Fizz")
    elif(i%5==0):
        print("Buzz")
    else:
        print(i)   '
'''        
#9.For multiples of 3, print "Fizz" instead of the number.
'''for i in range(1,51):
    if(i%3==0):
        print("Fizz")
    else:
        print(i)    
'''
#10.For multiples of 5, print "Buzz".
for i in range(1,51):
    if(i%5==0):
        print("Buzz")
    else:
        print(i)  
#11.For numbers that are multiples of both 3 and 5, print "FizzBuzz".
for i in range(1,51):
    if(i%3==0 and i%5==0):
        print("FizzBuzz")
    else:
        print(i)  

