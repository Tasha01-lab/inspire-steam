#Name: Tasha Margie Musau
#Date: 17/02/2026

#Program to format the output in different styles

name = "Tasha Margie Musau" # name

weight = 85 # weight in kgs

fav_team = "Arsenal"

height = 126.86 # height in cms

# 1. Format using print(f"{}")

print(f"My name is {name} and I weigh {weight} kgs.")

# 2. Using f string
msg = f"My name is {name} and I support {fav_team}"
print(msg)

# 3. Using {} and .format()
print("My name is {0} and I am {1} cms tall".format(name,height))

# 4. Using output specifiers %s -strings %f -float 
import math
print("The value of pi is approximately %5.3f" %math.pi)
print("I support %s " %fav_team)