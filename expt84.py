#!/usr/bin/python3
filename=input("Enter file name: ")
for line in reversed(list(open(filename))):
    print(line.rstrip())
