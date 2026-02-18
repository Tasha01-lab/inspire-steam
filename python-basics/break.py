#Name: Tasha Margie Musau
#Date: 17/02/2026

#Program to illustrate break in python

number = 1
while number <10 :
    print(number)
    number = number + 1 # or number += 1 or number = number +1 or number *= 2
    if number == 4:
        break
    print("breaking from the loop")
    continue
