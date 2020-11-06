#!/usr/bin/python3
fname = input("Enter file name: ")
 
with open(fname, 'r') as f:
    for line in f:
        l=line.title()
        print(l)
