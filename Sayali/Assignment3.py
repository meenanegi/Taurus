import random
# firstName=input("Input your first Name")
# if (len(firstName)<=3):
#     print("Atleast 3 letters are needed for first Name")
# elif(len(firstName)>20):
#     print("Name should not be more than 20 chars long")
# else:
#     print("Name looks good")

#===========MILES TO KM CONVERSION =========================
# distance=input("Enter the distance: ")
# metrics=input("Enter m if the entered distance is in miles or enter k if the distance is in KM: ")
# metrics=metrics.upper()
# distance= float(distance)
#
# if (metrics=="M"):
#     print("Entered Distance " + str(distance) + " in miles")
#     distance=(distance/0.62137)
#     print("Distance in Km: "+str(round(distance,2)))
# elif(metrics=="K"):
#     print("Entered Distance " + str(distance) + " in km")
#     distance=(distance *0.62137)
#     print("Distance in miles :"+ str(round(distance,2)))
# else:
#     print(" Invalid metrics entered. Please enter m for miles or k for KM.")

#=================== GUESSING GAME =============================================

secretNumber=int((random.random())*10)

guessingcount=1
while(guessingcount<=3):
    userNumber=input("Guess the number between 1 and 10: ")
    if(int(userNumber)!=secretNumber):
        print("Wrong guess! Try again")
        guessingcount+=1
    else:
        print("Correct guess!")
        break
print("The number was: "+str(secretNumber))



