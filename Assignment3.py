#TUPLE CREATION
#1.Create a tuple named my_tuple containing at least five different elements (mix of integers, strings, and a float).
my_tuple=(41,"Hello",1.2,"World",10)
print(my_tuple)

#ACCESSING ELEMENTS
#2.Print the first and last element of my_tuple using indexing.Use negative indexing to access the second last element.
my_tuple=("Hello","World")
print("First element:",my_tuple[0])
print("Second element",my_tuple[-1])
print("second last element",my_tuple[-2])

#Tuple Slicing
#3.Slice and print the first three elements of my_tuple.Slice and print the last two elements.
my_tuple=(100,"Hi",200,"hello")
print("First three elements:",my_tuple[:3])
print("last two elements:",my_tuple[2:])

#Tuple Operations
#4.concatenate my_tuple with another tuple and print the result.
my_tuple=("hello")
another_tuple=("World")
print("Concatenation of:",my_tuple+another_tuple)

#5.Repeat my_tuple twice and print the result.
repeat=my_tuple*2
print("Repeated tuple:",repeat)

#Tuple Methods
#6.Find the index of a specific element in my_tuple and print it.
my_tuple=("chandu","Anu","Hema")
print(my_tuple.index("Anu"))

#7.Count the occurrences of a specific element in my_tuple and print it.
my_tuple=("chandu","Anu","Hema",300,"chandu")
print(my_tuple.count("chandu"))

#Tuple Packing and Unpacking
#8.Create a tuple with three elements and unpack them into individual variables.Print the unpacked values.
Packing_tuple=(1,"hello",8)
print("Unpacked values:",Packing_tuple)

#Tuple Iteration
#9.Use a loop to iterate through my_tuple and print each element.
my_tuple=(100,101,200)
for i in my_tuple:
    print(i)

#Tuple Usage
#10.Write a function that returns multiple values using a tuple.Call the function and print the returned tuple.
def person_info():
    name = "Chandrakala"
    age = 20
    city = "Vizag"
    return (name, age, city)
person_info = person_info()
print("Returned tuple from function:", person_info)




