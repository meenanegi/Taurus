firstname=input("Enter a First Name: ")
print(firstname)
if len(firstname)<3:
    print("Atleast 3 letters are needed for first name")
elif len(firstname)>20:
    print("Name should not be more than 20 chars long")
else:
    print("Name looks good")

