#!/usr/bin/python3
n=2
count=0
while(count!=50):
	i=2
	while(n%i!=0):
		i+=1
	if(n==i):
		print(n)
		count+=1
	n=n+1
