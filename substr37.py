#!/usr/bin/python3
string=str(input("Enter string:"))
sub_str=str(input("Enter word:"))
if(string.find(sub_str)==-1):
      print("Substring not found in string!")
else:
      print("Substring in string!")

