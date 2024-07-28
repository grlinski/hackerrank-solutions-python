



# Sherlock and Anagrams V1 Mk2
# https://www.hackerrank.com/challenges/sherlock-and-anagrams/problem?h_l=interview&playlist_slugs%5B%5D%5B%5D=interview-preparation-kit&playlist_slugs%5B%5D%5B%5D=dictionaries-hashmaps
"""

This is more of a mathematical problem than anything


Create every fragment
Sort fragments and input them into a dictionary




"""

from itertools import permutations, combinations


def triangularNumber(n):
    amount = n * (n + 1) / 2
    return int(amount)


def sortFragment(x):
    list1 = []
    for i in x:
        list1.append(i)
    list1.sort()
    s = ''
    for i in list1:
        s+=i
    return s



def createFragments(s,dict,length):

    for i in range(0,len(s)):
        if i+length>len(s):
            break
        frag = s[i:i+length]
        fs = sortFragment(frag)
        if fs in dict:
            dict[fs]+=1
        else:
            dict[fs]=1
    return dict


times = int(input())

for t in range(times):
    s = input()
    dict = {}
    for length in range(1,len(s)):
        dict = createFragments(s,dict,length)

    counter=0
    for i in dict:
        if (dict[i]) >1:
            x = dict[i]
            x-=1
            y = triangularNumber(x)
            counter+=y
            #print(i,dict[i])

    print(counter)























