distance = float(input("Enter distance : "))
unit = str(input("whether distance is in Miles or Km : "))
if distance == "M" or "m":
    print("Distance in Km is ", distance * 1.609)
elif distance == "K" or "k":
    print("distance in Miles is ", distance * 0.621)
print("wrong input.")
