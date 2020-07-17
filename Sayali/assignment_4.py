 # 1. print 5 to 15 for loop
# for x in range(5,16):
#     print(x);

#2. print table of 4
# for x in range(1,11):
#     print(x*4);

# 3. list of odd numbers
# odd=[];
# for x in range(95,121):
#     if(x%2!=0):
#         odd.append(x);
#
# print(odd);

# 4. dictionary mapping
dictWeekDays={
    "1" :"Monday",
    "2":"Tuesday",
    "3":"Wednesday",
    "4":"Thursday",
    "5":"Friday",
    "6":"Saturday",
    "7":"Sunday"
};
dayNumber=input("Enter the Day Number to retreive day: ");
if(int(dayNumber)>7 or int(dayNumber)<1):
   print("enter the day Number between 1 and 7");
else:
    print(dictWeekDays.get(dayNumber));

