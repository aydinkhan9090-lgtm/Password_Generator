import random
import string
print("WELCOME TO PASSWORD GENERATOR!😊")
all_characters=string.ascii_letters+string.digits+string.punctuation
Length=int(input("enter the length of password u want to generate:"))   
password="" 
for i in range(Length):
    password+=random.choice(all_characters)
print("your password is :",password)

# now strength check karne vaala 
if len(password)<6:
    print("paaword too weak 😅")
elif len(password)>10:
    print("password is strong💪")
else:
    print("password is moderate,if want stronger one try bigger than 10 characters 😏")


            #    THANKS FOR USING MY TOOL 