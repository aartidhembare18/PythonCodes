#!/usr/bin/python3
s1=str(input("Enter first string:"))
s2=str(input("Enter second string:"))
a=list(set(s1)^set(s2))
print("The different letters are:")
for i in a:
    print(i)
