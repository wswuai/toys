# -*- coding: utf-8 -*-
import matplotlib.pyplot  as plt
import csv

reader = csv.reader(file('/Users/xiaogo/Documents/res.csv',"rb"))

x1 = []
y1 = []
z = []

for line in reader:
    y1.append(int(line[0]))
    x1.append(int(line[1]))
    z.append(int(line[0])*int(line[1])/10)

plt.xlabel(u'记账笔数')
plt.ylabel(u'账本合计/数据量(x10)')
plt.bar([1,2,3],[1,2,4],width = .35) 
#plt.axis([0, 1000, 0, 200000])
plt.title(u'随手记账本数据统计', fontsize=16)
plt.savefig('power.png', dpi=75)
plt.show() 
#plt.pie(y1[0:3], explode = [0,0,.2,])
plt.show()
