from collections import namedtuple
from operator import attrgetter
import sys
import openpyxl

stopWord = []

def init() :
    stopWordPath = "G:\semester\semester 4-1\ML Lab\Dataset\StopWords.txt"
    with open(stopWordPath, 'r') as f:
        data = f.read()
        words = data.split()
        for w in words:
            stopWord.append(w)


def isStopWord( word ) :
    word = word.lower()
    if word in stopWord :
        return True
    return False

def katJhat( word ) :
    ret = ""
    for w in word :
        if w >= 'a' and w <='w' :
            ret += w
        if w >= 'A' and w <= 'W' :
            ret += w
    return ret

def getWordList( LIM ) :
    rootPath = "G:\semester\semester 4-1\ML Lab\Dataset\Fake_News_Detection\Fake_News_Detection"
    path = "\{}".format("fake_or_real_news.xlsx")
    path = rootPath + path

    book = openpyxl.load_workbook(path)
    sheet = book.active
    wordList = []
    for i in range(2 , LIM) :
        ch = 'C' + str(i)
        cell = sheet[ch]
        text = cell.value
        word = ""
        for ch in text :
            if ch != ' ' :
                word += ch
            else:
                word = katJhat(word)
                if isStopWord(word) == False :
                    wordList.append(word)
                word = ""
    return wordList

def getMostFreqWordList( Words ) :
    uniqueWords = set(Words)
    myType = namedtuple("myType" , "word , count")
    ResultArray = []
    TempArray = []
    for word in uniqueWords :
        sample = myType(word=word , count=Words.count(word))
        TempArray.append(sample)
    ResultArray = sorted(TempArray , key=attrgetter("count") , reverse=True)
    return ResultArray