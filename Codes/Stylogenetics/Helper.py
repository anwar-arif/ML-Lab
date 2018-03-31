from collections import namedtuple
from operator import attrgetter
rootPath = "G:\semester\semester 4-1\ML Lab\Dataset\Stylogenetics\Stylogenetics\All Data"

def isEnglishWord(word) :
    for i in range(ord('a') , ord('z') + 1 ) :
        ch = chr(i)
        if ch in word :
            return True
    for i in range(ord('A') , ord('Z') + 1 ) :
        ch = chr(i)
        if ch in word :
            return True
    return False

# Removes punctuations from a word
def katJhat( word ) :
    ret = ""
    if isEnglishWord(word) :
        return ret
    for ch in word :
        if ch == '.' or ch == ',' or ch == '-' or ch == '-' or ch == '?' or ch == '।' or ch == '\n' or ch == ':':
            continue
        elif ch != ' ':
            ret += ch
    return ret

def textToWord(path) :
    wordList = []
    try:
        with open(path, 'r', encoding='utf-8') as f:
            data = f.read().split()
            for word in data:
                word = katJhat(word)
                wordList.append(word)
    except Exception:
        nothing = 0
    return wordList

def getMostFrequentWordList( writerName , LIM ) :
    wordList = []
    for i in range(1 , LIM) :
        path = rootPath + "\{}\{}".format(writerName, writerName) + str(i) + ".doc"
        try:
            with open(path, 'r', encoding='utf-8') as f:
                data = f.read().split()
                for word in data:
                    word = katJhat(word)
                    wordList.append(word)
        except Exception :
            nothing = 0
    uniqueWord = set(wordList)
    TempArray = []
    myType = namedtuple("myType", "word , count")
    for word in uniqueWord :
        sample = myType(word = word , count=wordList.count(word))
        TempArray.append(sample)
    ResultArray = sorted(TempArray, key = attrgetter("count") , reverse=True)
    return ResultArray