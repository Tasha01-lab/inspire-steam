#Name: Tasha Margie Musau
#Date: 12/02/2025

#String formatting

#Get string length 
sentence = "I watch anime"

string_length = len(sentence)

print(f"The length is: {string_length}")

#Splitting a string 
sentence_2 = "Mathematics Physics"
split = sentence_2.split(" ")

print(f"the first subject is: ",split[0])

#Make everything CAPS
mpesa_code = "ub21ddsfhg"

capitalized = mpesa_code.upper()

print("New mpesa code: ",capitalized)

#Make everything lower
mpesa_code = "UB21DDSFHG"

small = mpesa_code.lower()

print("New mpesa code: ",small)

#Replacing characters in a string

balance = "100Kes"
amount_added = "50Kes"

cleaned_balance = balance.replace("Kes", "")

print("Cleaned balance: ",cleaned_balance)

cleaned_amount_added = amount_added.replace("Kes", "")

print("Cleaned amount added: ", cleaned_amount_added)

#Adding the amount to get a total balance

new_balance = int(cleaned_balance) + int(cleaned_amount_added)
print("The new balance is: ",new_balance)

#Assignment
sentence_mpesa = "CONFIRMED you have received 40KES from Philip"

split1 = sentence_mpesa.split(" ")

print("Split 1 contents: ", split1)

print("the amount is: ",split1[4])

amount_added1 = split1[4]

cleaned_amount_added1 = amount_added1.replace("KES", "")

print("Cleaned amount added: ",cleaned_amount_added1)

balance1 = 50

new_balance1 = int(balance1) + int(cleaned_amount_added1)

print("New balance = ",new_balance1)