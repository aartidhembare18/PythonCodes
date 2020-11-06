#!/usr/bin/python3
class p(object):
	def __init__(self,x):
		self.x = x
		#self.y = y
	def __str__(self):
		return("{0}".format(self.x))
	def __lt__(self,object1):
		x=self.x<object1.x 
		return p(x)
	def __gt__(self,object1):
		x=self.x>object1.x 
		return p(x)
	def __ge__(self,object1):
		x=self.x>=object1.x 
		return p(x)
	def __le__(self,object1):
		x=self.x<=object1.x 
		return p(x)
	def __ne__(self,object1):
		x=self.x!=object1.x 
		return p(x)
	def __and__(self,object1):
		x=self.x&object1.x 
		return p(x)
	def __or__(self,object1):
		x=self.x|object1.x 
		return p(x)
	def __xor__(self,object1):
		x=self.x^object1.x 
		return p(x)
p2=p(2)
p1=p(3)
print(p1>p2)
print(p1<p2)
print(p1<=p2)
print(p1>=p2)
print(p1!=p2)
print(p1&p2)
print(p1|p2)
print(p1^p2)

