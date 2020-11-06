#!/usr/bin/python3
string=str(input("Enter string:"))
l=[]
l=string.split()
wordfreq=[l.count(p) for p in l]
print(dict(zip(l,wordfreq)))

