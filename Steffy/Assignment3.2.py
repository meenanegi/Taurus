#Program 2: Covert Miles to KM

d=input("Enter distance: ")
d=int(d)
v=input("Enter the unit of distance [M-Miles or K-Km]")

if v=="M" or v=="m":
    result=1.6*d
    v="miles"
    rv="km"
elif v=="K" or v=="k":
    result=0.621*d
    v="km"
    rv="miles"
else:
    print("Invalid unit of distance")

print(str(d)+str(v)+" = "+str(result)+str(rv))
