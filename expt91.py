#!/usr/bin/python3
import abc
class shape(abc.ABC):
	@abc.abstractmethod
	def area(self):
		pass
	@abc.abstractmethod
	def perimeter(self):
		pass
class rectangle(shape):
	def __init__(self,l,h):
		self.l=l
		self.h=h
	def area(self):
		area=self.l*self.h
		print("area=",area)
	def perimeter(self):
		perimeter=2*(self.l+self.h)
		print("perimeter=",perimeter)
class square(rectangle):
	def __init__(self,side):
		super().__init__(side,side)
r1=rectangle(2,4)
r1.area()
r1.perimeter()
s1=square(5)
s1.area()
s1.perimeter()
