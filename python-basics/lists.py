#Name: Tasha Margie Musau
#Date: 18/02/2026

#Program to show lists in python

#List of friends
friends = ["Rachel","Phoebe","Ross","Chandler","Monica","Joey"]
print(friends)

#Sort - sorts in alphabetical order
friends.sort()
print(friends)

#Reverse - reverses the order of the list
friends.reverse()
print(friends)

#Append - adds Jack to the far end of the list
friends.append("Jack")
print(friends)

new_friends = ["Tracy","James","Faith","Don","Augustine","Wendy"]

#Len - gives the number of elements in the list
print(len(new_friends))

#new list of students - adding two lists
students = friends + new_friends
print(students)

#Pop - removes the last item in the list i.e Wendy is removed from the list
students.pop()
print(students)

#Insert - inserts an element at a stated position on the list
students.insert(5,"Jenny") #Starts counting from zero, 5 - the fifth location
print(students)

#Challenge
students.insert(9,"Valery")
print(students)

#Extend - adds one element to the list where its added as separate characters
students.extend("James")
print(students)

#Remove - remove an element in the list
students.remove("Joey")
print(students)

#Copy - copies all the elements in students into new_students
new_students = students.copy()

#Count - tells how many times an element appers on a list

#Index - tells the position of the element in the list
students.index("Ross")

