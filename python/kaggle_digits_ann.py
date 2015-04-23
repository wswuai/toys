import numpy as np
from nolearn.dbn import DBN



testRest = 3000


def binaryzation(image):
    a = 0.0
    ret = []
    for i in image:
        a += i
    avg = a / len(image)
    for i in image:
        if i > avg:
            ret += 255
        else:
            ret += 0
    return ret


print("loading txt...")
fil = file('train.csv')
fil.readline()

data = np.loadtxt(fil, delimiter=',', dtype=np.float)

digits_label = data[:, 0]
digits_image = data[:, 1:]

# digits_label = np.array([i[0] for i in data])
# digits_image = np.array([i[1:]/255.0 for i in data])

digits_image = map(binaryzation, digits_image)


print("file loading ok , prepare to train model")

# object of ANN model.

clf = DBN(
    [digits_image.shape[1], 500, 500, 10],
    learn_rates=0.01,
    learn_rate_decays=0.9,
    epochs=20,
    verbose=1,
)

# gnb.fit(digits_image[:-testRest],digits_label[:-testRest])
clf.fit(digits_image[:-testRest], digits_label[:-testRest])

#result = gnb.predict(digits_image[-testRest:])
result = clf.predict(digits_image[-testRest:])

print("the err rate : %.2f %%" % (100 * ((result != digits_label[-testRest:]).sum()) / float(testRest)) )

print("the result num %.2f " % (result != digits_label[-testRest:]).sum())

testTxt = file('test.csv')
testTxt.readline()

testData = np.loadtxt(testTxt, delimiter=',', dtype=np.int)
result2 = clf.predict(testData)
out = open('outputann.csv', 'wb')
count = 1
out.write(u'"ImageId","Label"\n')
for i in result2:
    out.write(repr(count) + ",")
    count += 1
    out.write(r'"' + repr(i) + r'"')
    out.write('\n')
out.close()
exit()
