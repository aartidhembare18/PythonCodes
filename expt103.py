#!/usr/bin/python3
class myError(Exception):
	def __init__(self,value):
		self.value=value
try:
	raise(myError(3*2))
except myError as e:
	print("a new exception occured ",e)
