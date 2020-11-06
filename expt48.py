#!/usr/bin/python3
def reverse(text):
    if len(text) <= 1:
        return text

    return reverse(text[1:]) + text[0]
string=str(input("enter  string"))
print("reverse string is",reverse(string))
