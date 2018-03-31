from sklearn.linear_model import LinearRegression
import time
import openpyxl
import string

# init stuffs
# total number of rows in the dataset
num_rows = 7819
# tmeporary variable for storing a single news word list
unique_words = []
# the final feature vector including frequency of words in each news, each row represents each news
frequency_count = []
# the unique words list of entire document
feature = []
# the temporary feature vector
feature2 = []
#temporary string
str = ""


# path calculation
rootPath = "C:\\Users\\Jamil88\\PycharmProjects\\Basic ML"
path = "\\fake_or_realMod.xlsx"
path = rootPath + path
#read FILE
book = openpyxl.load_workbook(path)
sheet = book.active
#start = time.time()
#a1 = sheet['B24']
#print("{}\n".format(a1.value))



# #print each row separately
# for j in range(2,3) :
#     for i in range(ord('A') , ord('D') + 1 ) :
#         ch = chr(i) + str(j)
#         a1 = sheet[ch]
#         print("{} ".format(a1.value))



# print only a substring
def printSubstring(str2):
    return str2[0:30]

# to find the word in the list and if not,then join the word with the list
def findAndJoinUniqueWords(str, wordList):
    for i in wordList:
        if str.lower() == i.lower():
            return
    wordList.append(str.lower())

# compare a given word with the unique words in the feature[], then increment the rowNumber'th row and idx column
def compareWithUniqueWordsList(str, rowNumber):
    #make a new row in the frequency_count to accomodate this row of frequencies
    num_array = []
    for idx in enumerate(feature):
        num_array.append(0)
    frequency_count.append(num_array)

    #now compare against each word
    for idx, word in enumerate(feature):
        if str == word:
            # the given word equals the unique word, now we increment this index of freq_count[]
            frequency_count[rowNumber][idx] += 1
        else : frequency_count[rowNumber][idx] = 0

# to remove punctuation and spaces and then return the unique words
def removePunctuation(sampleString):
    #number of words in the sentence
    wordCount = 0
    #this string will contain the individual words in each interval
    str = ""

    #searching char by char
    for word in sampleString:
        if word == ' ' :
            # now format the list to contain only unique words
            findAndJoinUniqueWords(str, unique_words)

            print (unique_words)
            #reset the word string
            str = ""
        elif word.isalnum():
            str += word
    print("words in the array : {0}".format(len(unique_words)))
    # the collection of unique words in the current news
    return unique_words

    #str = ''.join(e for e in sampleString if e.isalnum() == True or e == ' ')

# to remove punctuation and spaces
def removePunctuation2(sampleString):
    #number of words in the sentence
    wordCount = 0
    #this string will contain the individual words in each interval
    str = ""

    #searching char by char
    for word in sampleString:
        if word == ' ' :
            compareWithUniqueWordsList(str)
            #reset the word string
            str = ""
        elif word.isalnum():
            str += word
    print("words in the array : {0}".format(len(unique_words)))
    # the collection of unique words in the current news
    return unique_words

def processRows():
    # traverse each row of the excel sheet, row contains the info
    for idx_row, row in enumerate(sheet.rows):
        print("row number : {0}".format(idx_row))
        if idx_row > 10:
            print("breaking the operation after 10 rows")
            break
        for idx_col, col in enumerate(row):
            # for only the news column
            if idx_col == 1:
                # add the raw text of the news to the existing unique words list
                feature.append(col.value)
                # remove punctuation and also detect unique words in this row and then replace the raw news with this row's unique words
                feature[idx_row] = removePunctuation(col.value)
                # the current news in this row in unique words form
                print(feature[idx_row])

def createFeatureVector():
    for idx_row, row in enumerate(sheet.rows):
        if idx_row > 10:
            break
        for idx_col, col in enumerate(row):
            # for only the news column
            if idx_col == 1:
                # the raw text of the news
                feature2.append(col.value)
                # remove punctuation and also detect unique words in this news
                feature2[idx_row] = removePunctuation2(col.value)
                # the current news in this row in unique words form
                print(feature2[idx_row])
            # for only the class column
            if idx_col == 2:


# to find unique words from all the news rows
processRows()
# create the feature vector for individual rows
#createFeatureVector()


# # for the features of the model
# features = []
# for i in range( ord('B') , ord('T')) :
#     ch = chr(i) + '1'
#     a1 = sheet[ch]
#     features.append(a1.value)

# # Making training dataset
# X_train = []
# Y_train = []
# LIM = 10000
#
# for i in range(2 , LIM) :
#     temp = []
#     for j in range(ord('B') , ord('T')) :
#         ch = chr(j) + str(i)
#         a1 = sheet[ch]
#         temp.append(a1.value)
#     X_train.append(temp)
#     ch = 'T' + str(i)
#     a1 = sheet[ch]
#     Y_train.append(a1.value)
#
# # Fit the model with training dataset
# linreg = LinearRegression()
# linreg.fit(X_train , Y_train)
#
# # Testing
# X_test = []
# Y_test = []
#
# for i in range(LIM , LIM + 50) :
#     temp = []
#     X = []
#     for j in range(ord('B') , ord('T')) :
#         ch = chr(j) + str(i)
#         a1 = sheet[ch]
#         temp.append(a1.value)
#     X.append(temp)
#     pred = linreg.predict(X)
#     ch = 'T' + str(i)
#     a1 = sheet[ch]
#     expected = a1.value
#     print("{} => {}\n".format(pred , expected))
# endd = time.time()
# print("Execution Time {}\n".format(endd - start))