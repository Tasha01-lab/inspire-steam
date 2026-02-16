#Name: Tasha Margie Musau
#Date: 16/02/2026

#Program to calculate the factorial of numbers

number = int(input("Enter the number x: ")) #Get number from user
factorial = 1 #initialize factorial as 1
for x in range (0, number):
    factorial = factorial * (x+1)
    
print(f"{number}! = {factorial}")
