#!/bin/python3


n = int(input("Enter value Between 1 to 100 : "))
if(2<=n<=5 and n%2==0):
    print("Not Weird")
elif(6<=n<=20 and n%2==0):  
    print("Weird")
elif(n>20 and n%2==0):  
    print("Not Weird")
else:
    print("Weird")