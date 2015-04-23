# -*- coding: utf-8 -*-
import matplotlib.pyplot  as plt
import csv
import numpy as np
import segmentation
import sys

def seg():
    global stcounter
    reader = csv.reader(file('query2.csv',"rb"))
    for line in reader:
        yield float(line[0])
        #sys.stdout.write("\rReading ... (%d)" % reader.line_num)
        #sys.stdout.flush()



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

segs = [[1,10],[10,100],[100,1000],[1000,10000],[10000,100000],[100000,]]

ret = segmentation.seg(seg(),segs)

N = len(segs)
menStd =   (0)*N
 
ind = np.arange(N)*1  # the x locations for the groups
width = 0.55       # the width of the bars
 
fig, ax = plt.subplots()
rects1 = ax.bar(ind, ret, width, color='grey',align='center')
#rects2 = ax.bar(ind+1*width, z2, width, color='y', yerr=menStd)
 
ax.set_ylabel(u'用户数(人/次)')
ax.set_xlabel(u'应还款额(RMB)')
ax.set_title(u'卡牛区间统计')
ax.set_xticks(ind)
ax.set_xticklabels( ('1~10', '10~100', '100~1000', '1K~10K', '10K~100K','100K+') )
 
#ax.legend( (rects1[0], rects2[0],rects3[0]), ('All', '2014~now','2015~now') )

autolabel(rects1)
#autolabel(rects2)
#autolabel(rects3)
plt.show()

