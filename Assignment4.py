#Basic Operations:

#1.Create a set with at least five different numbers.
set={1,3,5,7,9}
print(set)
#2.Add an element to the set and remove an element from it.
set={1,2,3,4,5}
set.add(10)#add element
print(set)
set.remove(4)#remove element
print(set)
#3.Check if a given element exists in the set.
set={1,2}
print("Is 2 in the set:",2 in set)

#Set Operations:
#4.Write a Python program to find the union, intersection, and difference between two sets.
set1={1,2,3,4}
set2={3,4,5,6}
print("Union:",set1|set2)
print("Intersection:",set1&set2)
print("Difference:",set1-set2)
#5.Create two sets and determine if one is a subset of the other.
set1={1,2,3,4}
set2={3,4,5,6}
print(set1.issubset(set2))

#Unique Elements:
#6.Given a list with duplicate elements, convert it into a set to remove duplicates.
list1={1,2,3,3,5,6,6}
list2=list(list1)
print("Unique elements:",list2)

#Mathematical Applications:
#7.Create sets representing students enrolled in two different courses and find students who are in both courses
math={"chandu","puji","Anu","Hema","Sasi"}
computers={"thanu","latha","thanish","Hema","Sasi"}
both_courses=math&computers
print(both_courses)
#8.Write a program to find common elements between three sets.
set1={1,2,3,4}
set2={2,3,4}
set3={3,5,6}
common_elements=set1&set2&set3
print(common_elements)

#Set Comprehension:
#9.Use set comprehension to create a set of squares of numbers from 1 to 10.
squares={x*x for x in range(1,11)}
print("Squares from 1 to 10:",squares)

#Frozen Sets:
#10Explain and demonstrate the use of a frozenset in Python.
immutable_set=frozenset([1,2,3,4])
print(immutable_set)