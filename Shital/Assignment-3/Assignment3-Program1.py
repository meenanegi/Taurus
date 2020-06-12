Name = input("Enter your First Name: ")

if len(Name)<3:
    print("Atleast 3 letters are needed for first name")
elif len(Name)>20:
    print("Name should not be more than 20 chars long")
else:
    print("Name looks good")