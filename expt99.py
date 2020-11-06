#!/usr/bin/python3
while True:
	try:
		x=int(input("enter a number"))
		break
	except(RuntimeError,NameError,TypeError,ValueError):
		print("it's not integer  number")
while True:
	try:
		raise NameError("hii")
	except NameError:
		print("exception occured")
		raise
