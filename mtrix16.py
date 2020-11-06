#!/usr/bin/python3
p=int(input("enter total numbers in matrix"))
m=int(input("enter the numer of rows"))
n=int(input("enter the numer of colums"))
a=[]
for i in range(0,m):
	a.append([])
for i in range(0,m):
	for j in range(0,n):
		a[i].append([])
print("enter the elements of 2D array")
for i in range(0,m):
	for j in range(0,n):
		a[i][j]=int(input())
print("array elements are")
for i in range(0,m):
	for j in range(0,n):
		print(a[i][j],end=" ")
	print()

for s in range(0,p):
	for i in range(0,m):
		for j in range(0,n):
			if(i==j):
				print("diagonal elements of matrix are",a[i][j])
	

