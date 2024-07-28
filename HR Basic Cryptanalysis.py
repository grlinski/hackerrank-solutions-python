
# Basic Cryptanalysis
# https://www.hackerrank.com/challenges/basic-cryptanalysis/problem
"""
No idea where the dictionary.lst is
So instead I'll do this via letter freq
Actually it states in the problem that freq won't help as these are technical jargon
Not common words


TO DO
Look Up:
string isomorphism

May Work
Just too slow


TO DO 2
Incorporate alpha dict into findmatch




"""


def alphabet(alpha,word,match):
    match = match[0]
    for i in range(0,len(word)):
        alpha[word[i]] = match[i]

    return alpha


def findMatch(candidates,word):
    #print('FindMatchWord',word)
    shortList = {}


    for c in candidates:
        dictc = {}
        dictw = {}
        listc = []
        listw = []
        numc = 0
        numw = 0

        for i in range(0,len(c)):
            curc = c[i]
            curw = word[i]

            if curc in dictc:
                listc.append(dictc[curc])
            else:
                dictc[curc] = numc
                listc.append(dictc[curc])
                numc+=1
            if curw in dictw:
                listw.append(dictw[curw])
            else:
                dictw[curw] = numw
                listw.append(dictw[curw])
                numw+=1
        if listw == listc:
            if word in shortList:
                shortList[word].append(c)
            else:
                shortList[word] = [c]

    return shortList[word]


def translate(alpha,word):
    newWord = ''

    for i in word:
        if i in alpha:
            newWord+=(alpha[i])
        else:
            newWord+=i
    return newWord






dict1 = {}
listofWords = 'dictionary.txt'
list1 = open(listofWords, "r")
x = list1.readlines()
allWords = []
total = 0
for i in x:
    if i !='':
        y = i[:-1]
        if y == '':
            pass
        else:
            y = y.lower()
            leng = len(y)
            total+=1
            if leng in dict1:
                dict1[leng].append(y)
            else:
                dict1[leng] = [y]

s = input().split(' ')
shortList = {}
alpha = {}




for i in s:
    shortList[i] = findMatch(dict1[len(i)],i)
    if len(shortList[i]) == 1:
        alpha = alphabet(alpha,i,shortList[i])

ansList = []
for i in s:
    x = translate(alpha,i)
    print(x,end=' ')
for i in shortList:
    print(i,shortList[i])