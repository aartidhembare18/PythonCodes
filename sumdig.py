#!/usr/bin/python3
n=int(input("enter the number"))
num=0
while(n>0):
	dig=n%10
	num=num+dig
	n=n//10
print("the total sum of digits:",num)
