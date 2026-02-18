#Name: Tasha Margie Musau
#Date: 18/02/2026

#Program to show tuples in python

fruits = ("Avocado","Kiwi","Apples","Banana","Orange")

print(len(fruits))
print(fruits[0])#Starts counting at 0
print(fruits[4])
print(fruits[-1])#Starts counting from the last element
print(fruits[-5])

#In tuples you cant append, pop or the rest because its immutable
#Immutable - can not change list
#error -> fruits.append("Guava")

fruits_list = list(fruits) #converts a tuple to a list
fruits_list.append("Guava")
print(fruits_list)
