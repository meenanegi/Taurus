
# Assignment 4 - Week 4
# Program 1 - Print numbers from 5 to 15 using for loop

print("Program 1 - Print numbers from 5 to 15 using for loop")
for i in range(5, 16):
    print(i)

# Program 2 - print tables of 4
print("Program 2 - print tables of 4")
for i in range(1,11):
    print(f"4 x {i} = {4*i}")

# Program 3 - Print all the odds numbers from 95 to 120 in a list.
# Use append to add the number in a list and the output should be a list.

print("Program 3 - Print all the odds numbers from 95 to 120 in a list. Use append to add the number in a list and the output should be a list.")
arr=[]
for i in range(95,121):
    if i%2!=0:
        arr.append(i)
print(arr)

# Program 4 - Create a dictionary mapping day number with actual day starting 1 as monday . E.g {"1": "Monday", "2": "Tuesday"}
# take input from the user and if user enter the value "2", the output should print "Tuesday".

print("Program 4 - Create a dictionary mapping for a week")
week={1:"Monday",
      2:"Tuesday",
      3:"Wednesday",
      4:"Thursday",
      5:"Friday",
      6:"Saturday",
      7:"Sunday"}
dayofweek=input("Enter day of the week (1-7): ")
dayofweek=int(dayofweek)
if dayofweek<1 or dayofweek>7:
    print("Invalid input")
else:
    print(f"Day = {week[dayofweek]}")
