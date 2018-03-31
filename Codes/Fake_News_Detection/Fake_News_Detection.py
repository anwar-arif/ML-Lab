import Helper
import openpyxl
import time
from sklearn import svm

start_time = time.time()

rootPath = "G:\semester\semester 4-1\ML Lab\Dataset\Fake_News_Detection\Fake_News_Detection"
path = "\{}".format("fake_or_real_news.xlsx")
path = rootPath + path

book = openpyxl.load_workbook(path)
sheet = book.active

# Initilize stopwordList
Helper.init()

LIM = 100
MaxFeature = 3000
Feature = []

wordList = Helper.getWordList(LIM)
uniqueWord = set(wordList)

TempArray = Helper.getMostFreqWordList(wordList)

cnt = 0
for temp in TempArray :
    Feature.append(temp.word)
    cnt += 1
    if cnt > MaxFeature :
        break
# Train the dataset with SVM
X_train = []
Y_train = []

for i in range(2 , LIM) :
    ch = 'C' + str(i)
    cell = sheet[ch]
    text = cell.value

    ch2 = 'D' + str(i)
    cell2 = sheet[ch2]
    text2 = cell2.value

    temp = []
    for f in Feature :
        if f in text :
            temp.append(1)
        else:
            temp.append(0)
    X_train.append(temp)
    if "REAL" in text2:
        Y_train.append(1)
    if "FAKE" in text2:
        Y_train.append(0)

clf = svm.SVC()
clf.fit(X_train , Y_train)


total = 0
success = 0

for i in range(LIM , LIM + 10) :
    ch = 'C' + str(i)
    cell = sheet[ch]
    text = cell.value

    ch2 = 'D' + str(i)
    cell2 = sheet[ch2]
    text2 = cell2.value
    expected = 1
    if "FAKE" in text2:
        expected = 0
    X = []
    temp = []
    for f in Feature :
        if f in text :
            temp.append(1)
        else:
            temp.append(0)

    X.append(temp)
    pred = clf.predict(X)
    if pred[0] == expected :
        success += 1
    total += 1
    print("{} {}\n".format(pred[0] , expected))

print("Total {} correct {} accuracy {}\n".format(total , success , success/total))

end_time = time.time()
print("Execution Time {} Seconds\n".format(end_time - start_time))
