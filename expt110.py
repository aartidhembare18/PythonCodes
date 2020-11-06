#!/usr/bin/python3
import matplotlib.pyplot as p
labels=['A','B','C','D']
sizes=[15,20,95,15]
explode=[0,0.1,0,0]
fig1,ax1=p.subplots()
ax1.pie(sizes,explode=explode,labels=labels,shadow=True,startangle=90)
#ax1.axis("equal")
p.show()
