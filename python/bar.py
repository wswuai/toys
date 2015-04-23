# -*- coding: utf-8 -*-
import matplotlib.pyplot  as plt
import csv
import numpy as np

def autolabel(rects):
    # attach some text labels
    for rect in rects:
        height = rect.get_height()
        if(height > 1000):
            ax.text(rect.get_x()+rect.get_width()/2., 1.02*height, '%.0fK'%float(height/1000.00),
                ha='center', va='bottom')
        else:
            ax.text(rect.get_x()+rect.get_width()/2., 1.02*height, '%d'%int(height),
                ha='center', va='bottom')


reader = csv.reader(file('/Users/xiaogo/Documents/res.csv',"rb"))
reader1 = csv.reader(file('/Users/xiaogo/Documents/res2014tonow.csv',"rb"))
reader2 = csv.reader(file('/Users/xiaogo/Documents/res2015tonow.csv',"rb"))
x1 = []
y1 = []
z1 = [0,0,0,0,0,0]

x2 = []
y2 = []
z2 = [0,0,0,0,0,0]

x3 = []
y3 = []
z3 = [0,0,0,0,0,0]

for line in reader:
    y1.append(int(line[0]))
    x1.append(int(line[1]))

for line in reader1:
    y2.append(int(line[0]))
    x2.append(int(line[1]))

for line in reader2:
    y3.append(int(line[0]))
    x3.append(int(line[1]))

# x1: 账本笔数，y1:账本总数


for x in range(0,len(x1)):
    if(x1[x]>=1 and x1[x]<10):
        z1[0]=y1[x]+z1[0]
    if(x1[x]>=10 and x1[x]<100):
        z1[1]=y1[x]+z1[1]
    if(x1[x]>=100 and x1[x]<1000):
        z1[2]=y1[x]+z1[2]
    if(x1[x]>=1000 and x1[x]<10000):
        z1[3]=y1[x]+z1[3]
    if(x1[x]>=10000 and x1[x]<100000):
        z1[4]=y1[x]+z1[4]
    if(x1[x]>=100000 and x1[x]<1000000):
        z1[5]=y1[x]+z1[5]

for x in range(0,len(x2)):
    if(x2[x]>=1 and x2[x]<10):
        z2[0]=y2[x]+z2[0]
    if(x2[x]>=10 and x2[x]<100):
        z2[1]=y2[x]+z2[1]
    if(x2[x]>=100 and x2[x]<1000):
        z2[2]=y2[x]+z2[2]
    if(x2[x]>=1000 and x2[x]<10000):
        z2[3]=y2[x]+z2[3]
    if(x2[x]>=10000 and x2[x]<100000):
        z2[4]=y2[x]+z2[4]
    if(x2[x]>=100000 and x2[x]<1000000):
        z2[5]=y2[x]+z2[5]

for x in range(0,len(x3)):
    if(x3[x]>=1 and x3[x]<10):
        z3[0]=y3[x]+z3[0]
    if(x2[x]>=10 and x3[x]<100):
        z3[1]=y3[x]+z3[1]
    if(x3[x]>=100 and x3[x]<1000):
        z3[2]=y3[x]+z3[2]
    if(x3[x]>=1000 and x3[x]<10000):
        z3[3]=y3[x]+z3[3]
    if(x3[x]>=10000 and x2[x]<100000):
        z3[4]=y3[x]+z3[4]
    if(x3[x]>=100000 and x2[x]<1000000):
        z3[5]=y3[x]+z3[5]

N = 6
menStd =   (0)*6
 
ind = np.arange(N)*3  # the x locations for the groups
width = 0.75       # the width of the bars
 
fig, ax = plt.subplots()
rects1 = ax.bar(ind, z1, width, color='r', xerr=menStd)
 
womenStd =   (5, 5, 5, 5, 5,5)
rects2 = ax.bar(ind+1*width, z2, width, color='y', yerr=menStd)
rects3 = ax.bar(ind+2*width, z3, width, color='b', yerr=menStd)
 
ax.set_ylabel(u'账本总数（本）')
ax.set_xlabel(u'记账数（条）')
ax.set_title(u'随手记账本统计')
ax.set_xticks(ind+width)
ax.set_xticklabels( ('1~10', '10~100', '100~1000', '1K~10K', '10K~100K','100K+') )
 
ax.legend( (rects1[0], rects2[0],rects3[0]), ('All', '2014~now','2015~now') )

autolabel(rects1)
autolabel(rects2)
autolabel(rects3)
plt.show()
