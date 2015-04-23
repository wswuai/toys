import csv
import sklearn.naive_bayes as nb
import numpy as np
import sys
import pandas
import sklearn.svm


testRest = 3000

def binaryzation(image):
    a = 0.0
    ret = []
    for i in image:
        a += i
    avg = a/len(image)
    for i in image:
        if(i > avg):
            ret += 255
        else:
            ret += 0
    return ret


print("loading txt...")
fil = file('train.csv')
fil.readline()

txt = np.loadtxt(fil, delimiter=',',dtype=np.int)

data = txt

digits_label = [i[0] for i in data]
digits_image = [i[1:] for i in data]

digits_image = map(binaryzation, digits_image)
print("file loading ok , prepare to train model")

#gnb = nb.MultinomialNB()
gnb = sklearn.svm.LinearSVC()

gnb.fit(digits_image[:-testRest],digits_label[:-testRest])

result = gnb.predict(digits_image[-testRest:])

print("the err rate : %.2f %%" % (100*((result != digits_label[-testRest:]).sum())/float(testRest)) )


print("the result num"%(result!= digits_label[-testRest:]).sum() )

testTxt = file('test.csv')
testTxt.readline()

testData = np.loadtxt(testTxt,delimiter=',',dtype=np.int)
result2 = gnb.predict(testData)

out = open('output.csv','wb')
count = 1
out.write(u'"ImageId","Label"\n')
for i in result2:
    out.write(repr(count) + ",")
    count +=1
    out.write(r'"'+repr(i)+r'"')
    out.write('\n')
out.close()
exit()
