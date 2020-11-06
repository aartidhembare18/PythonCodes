#!/usr/bin/python3
class p(object):
	def __init__(self,x,y):
		self.x = x
		self.y = y
	def __str__(self):
		return("{0},{1}".format(self.x,self.y))
	def __add__(self,object1):
		x=self.x+object1.x 
		y=self.y+object1.y
		return p(x,y)
	def __sub__(self,object1):
		x=self.x-object1.x 
		y=self.y-object1.y
		return p(x,y)
	def __truediv__(self,object1):
		x=self.x/object1.x 
		y=self.y/object1.y
		return p(x,y)
	def __floordiv__(self,object1):
		x=self.x//object1.x 
		y=self.y//object1.y
		return p(x,y)
	def __mod__(self,object1):
		x=self.x%object1.x 
		y=self.y%object1.y
		return p(x,y)
	def __mul__(self,object1):
		x=self.x*object1.x 
		y=self.y*object1.y
		return p(x,y)
p1=p(2,3)
p2=p(2,3)
print(p1+p2)
print(p1-p2)
print(p1/p2)
print(p1//p2)
print(p1%p2)
print(p1*p2)
