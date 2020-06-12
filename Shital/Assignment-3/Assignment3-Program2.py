Distance = float(input("Enter the distance: "))
Input = str(input("Whether its Miles or Km: "))

if Input =="M":
    Distance=Distance*1.609
    print(f"Distance in Km {Distance}")
elif Input == "K":
    Distance=Distance*0.621
    print(f"Distance in Miles {Distance}")
else:
    print("Invalid Input")
