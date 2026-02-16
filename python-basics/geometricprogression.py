#Name: Tasha Margie Musau
#Date: 13/02/2026

#Program to calculate geometric progression

#a = first term, n = number of terms, r = common ratio

a = int(input("Enter the first term : "))
n = int(input("Enter the number of terms : "))
r = int(input("Enter the common ratio : "))

nth_term = a * (r**(n - 1))

print(f"The nth_term is : {nth_term}")

