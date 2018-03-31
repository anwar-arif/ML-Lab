from collections import namedtuple
from operator import attrgetter
from sklearn.naive_bayes import GaussianNB
import time
import Helper
rootPath = "G:\semester\semester 4-1\ML Lab\Dataset\Stylogenetics\Stylogenetics\All Data"
writers = ["emon_jubayer" , "hasan_mahbub" , "MZI" , "nir_nhondhani"]
# Minimum files for each writers is 120
LIM = 20
FeatureLim = 30
nothing = 0
start_time = time.time()

Features = []
for writer in writers :
    result = Helper.getMostFrequentWordList(writer , LIM)
    temp = []
    for i in range(1 , FeatureLim ) :
        temp.append(result[i].word)
    Features = set(Features) | set(temp)
    # for word in temp :
    #     print("{} ".format(word))
    # print("\n")

print("------Features-------\n")
# for f in Features :
#     print("{}".format(f))
print("Feature Size {}\n".format(len(Features)))

X_train = []
Y_train = []

X_test = []
Y_test = []

for writer in writers :
    for i in range(1 , LIM) :
        path = rootPath + "\{}\{}".format(writer, writer) + str(i) + ".doc"
        temp = Helper.textToWord(path)
        tempX = []
        for f in Features:
            if f in temp:
                tempX.append(1)
            else:
                tempX.append(0)
        X_train.append(tempX)
        Y_train.append(writer)

clf = GaussianNB()
clf.fit(X_train , Y_train)


total = 0
success = 0

for writer in writers :
    for i in range(LIM , LIM + 15) :
        path = rootPath + "\{}\{}".format(writer, writer) + str(i) + ".doc"
        temp = Helper.textToWord(path)
        tempX = []
        for f in Features:
            if f in temp :
                tempX.append(1)
            else:
                tempX.append(0)
        X_test = []
        X_test.append(tempX)
        pred = clf.predict(X_test)
        total += 1
        if writer in pred :
            success += 1
        print("{} => {}".format(pred , writer))

print("Total {} success {} accuracy {}\n".format(total , success , success/total))
end_time = time.time()
print("Execution Time = {}\n".format(end_time - start_time))