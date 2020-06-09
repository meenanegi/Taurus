first_name = str(input("enter your first name : "))
if len(first_name) < 3:
    print("Atlest 3 letter are needed for first name")
elif len(first_name) > 20:
    print("First name should not have more than 20 chars long")
else:
    print("Name looks good")
