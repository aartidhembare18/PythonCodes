#!/usr/bin/python3
n=int(input("enter the number"))
count=0
while(n>0):
	dig=n%10
	count+=1
	n=n//10
print("the total sum of digits:",count)
