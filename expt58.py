#!/usr/bin/python3
mydict = {'carl':40,
          'alan':2,
          'aaob':1,
          'danny':3}

for key in sorted(mydict.keys()):
    print("%s: %d" % (key, mydict[key]))
