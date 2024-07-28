
# Weighted Uniform Strings Mk2

# https://www.hackerrank.com/challenges/weighted-uniform-string/problem
# To make this not timeout I switched all from a list to a set()
# Sets do not contain duplicate info and are unordered

def uniform(s,list1):
    q = []
    all = set()
    for i in s:
        j = ord(i)-96
        q.append(j)
    endvalue = len(q)-1
    start = 0
    end = len(q)


    total = 0
    prev = q[0]
    for i in range(start,len(q)):
        x = q[i]
        if x == prev:
            total = total+x
            all.add(total)
        else:
            total = x
            all.add(total)
        prev = x

    for i in list1:
        if i in all:
            print("YES")
        else:
            print("NO")
    #print(all)









list1 = [6,1,3,12,5,9,10]
s = 'abccddde'

uniform(s,list1)






