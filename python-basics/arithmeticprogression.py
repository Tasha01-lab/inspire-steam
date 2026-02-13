#Name: Tasha Margie Musau
#Date: 13/02/2026

#Program to calculate arithmetic progression

#Calculate the nth term and the sn term

#a = first term, n = number of terms, d = common difference

a = int(input("Enter the first term : "))
n = int(input("Enter the number of terms : "))
d = int(input("Enter the common difference : "))

nth_term = a + (n - 1) * d
sn = (n/2) * ( (2*a) + (n - 1) * d)
print(f"The nth_term is : {nth_term}")
print(f"The sn term is : {sn}")
