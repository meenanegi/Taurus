# number1= input("Enter the first number: ");
# number1=float(number1);
#
# number2=input("Enter the second number: ");
# number2=float(number2);
#
# def add(val1,val2):
#      return val1+val2;
#
# def subtract(val1,val2):
#      return val1-val2;
#
# def multiply(val1,val2):
#     return val1*val2;
#
# def divide(val1,val2):
#     return val1/val2;

# print(f" addition: {add(number1,number2)}" );
# print(f" Subtraction: {subtract(number1,number2)}" );
# print(f" Multiplication: {multiply(number1,number2)}" );
# print(f" division: {format(divide(number1,number2),'.2f')}" );

###################### 2. total of list items ###########in

# price_list=[];
# count= input("Enter the total number of items in price list: ");
# count=int(count);
#
# for i in range(0,count):
#     item=input("Enter the price of item: ");
#     price_list.append(float(item));
#
# def calculatePrice(lstItems):
#     sum=0;
#     for x in lstItems:
#         sum=sum+x;
#     print(f" total price of items in the price list is: {sum}");
#
# calculatePrice(price_list);

################### 3.  Print item in Dict #######
dictItems={};

n=int(input("Enter the total number of items in Dictionary: "));
for i in range(n):
    k=float(input("Enter the price  for fruites: "));
    v=input("Enter the fruites: ");
    dictItems[k]=v;


def displayGreaterThanFifty(dictFruites):
    for i,j in dictFruites.items():
        if(i>50.0):
            print(f"fruit: {j} for price {i}");

def printList(dict_A):
    for i,j in dict_A.items():
        print(f" Fruit: {j}  Price : {i}");

printList(dictItems);

print("List of all fruites with price greater Than 50: ");
displayGreaterThanFifty(dictItems);







