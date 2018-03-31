from sklearn.linear_model import LinearRegression
import time
import openpyxl
rootPath = "G:\semester\semester 4-1\ML Lab"
path = "\Dataset\Apartment_Price_Prediction\Apartment_Price_Prediction\Houses data.xlsx"
path = rootPath + path

book = openpyxl.load_workbook(path)
sheet = book.active
start = time.time()

features = []
for i in range( ord('B') , ord('T')) :
    ch = chr(i) + '1'
    a1 = sheet[ch]
    features.append(a1.value)

# Making training dataset
X_train = []
Y_train = []
LIM = 10000

for i in range(2 , LIM) :
    temp = []
    for j in range(ord('B') , ord('T')) :
        ch = chr(j) + str(i)
        a1 = sheet[ch]
        temp.append(a1.value)
    X_train.append(temp)
    ch = 'T' + str(i)
    a1 = sheet[ch]
    Y_train.append(a1.value)

# Fit the model with training dataset
linreg = LinearRegression()
linreg.fit(X_train , Y_train)

# Testing
X_test = []
Y_test = []

total = 0
error = 0
for i in range(LIM , LIM + 50) :
    temp = []
    X = []
    for j in range(ord('B') , ord('T')) :
        ch = chr(j) + str(i)
        a1 = sheet[ch]
        temp.append(a1.value)
    X.append(temp)
    pred = linreg.predict(X)
    ch = 'T' + str(i)
    a1 = sheet[ch]
    expected = a1.value
    error += ( abs(pred[0] - expected) / expected )
    total += 1
    print("{} => {} {}\n".format(pred[0] , expected , abs(pred[0] - expected) / expected))

error = (error / total)
accuracy = 1.0 - error
print("Accuracy {}\n".format(accuracy))

endd = time.time()
print("Execution Time {}\n".format(endd - start))