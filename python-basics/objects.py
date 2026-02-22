#Name: Tasha Margie Musau
#Date: 19/02/2026

#Classes (objects) in python

class Human:
    # First we define the attributes of a human being
    type = "Mammal"
    legs = 2
    brain = True
    warm_blooded = True
    city = "Nairobi"

    # We then create a constructor for the class/object
    # The constructor will be used to create copies of the object
    def __init__(self, name, age): #constructor
        self.human_name = name
        self.human_age = age

    def tell_story(self):
        print(f"Hello, I am {self.human_name} Here is a story")
        print("There was once a bot that said Hello world")

#Create the humans       
amani = Human("Amani",17)
triza = Human("Triza",16)  

#Let the humans created do things
amani.tell_story()
print("Amani's age is: ", amani.human_age)

#Modify one of the objects without modifying other objects
print("Triza's location: ", triza.city)
print("Amani's location: ", amani.city)

triza.city = "Kiambu"

print("Triza's location: ", triza.city)
print("Amani's location: ", amani.city)