#!/usr/bin/python3
def modify(string,n):  
	final=""   
	for i in range(1,n):  
		if i%2==0:  
			final=final+string[i]  
	return final
def even(string,n):
	odd=""
	for j in range(0,n):
		if j%2!=0:
			odd=odd+string[j]
	return odd
string=str(input("Enter string:"))
n=len(string)
print("Modified string is:")
print(modify(string,n))
print("Modified string is:")
print(even(string,n))


