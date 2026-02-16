#Name: Tasha Margie Musau
#Date: 12/02/2026

#Program to use strings to show new balance


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