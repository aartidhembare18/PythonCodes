#!/usr/bin/python3
class print1():
    def __init__(self):
        self.string=""
 
    def get(self):
        self.string=input("Enter string: ")
 
    def display(self):
        print("String is:")
        print(self.string)
 
obj=print1()
obj.get()
obj.display()
