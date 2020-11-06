#!/usr/bin/python3
x=int(input("enter dividend"))
y=int(input("enter divisor"))
try:
	result=x/y
except ZeroDivisionError:
	print("zero divide error")
else:
	print("result is", result)
finally:
	print("finally block always executed")
	
