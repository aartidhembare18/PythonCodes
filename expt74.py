#!/usr/bin/python3
def check(string,ch):
      if not string:
        return 0
      elif string[0]==ch:
            return 1+check(string[1:],ch)
      else:
            return check(string[1:],ch)
string=str(input("Enter string:"))
ch=str(input("Enter character to check:"))
print("Count is:")
print(check(string,ch))
