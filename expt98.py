#!/usr/bin/python3
def divide(x,y):
	try:
		result=x/y
	except Exception as e:
		print(e)

	else:
		print("result is",result)
	finally:
		print("finally always executed")
	
divide(2,0)
