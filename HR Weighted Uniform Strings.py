
# Weighted Uniform Strings
# I forgot that the substrings can only consist of one letter
# However this so far is a pretty decent algorithm I'd like to keep
# Turns every substring into a number
# Not 100% complete
# Many inefficiencies


# https://www.hackerrank.com/challenges/weighted-uniform-string/problem


def uniform(s):
    q = []
    all = []
    for i in s:
        j = ord(i)-96
        q.append(j)
        all.append(j)
    endvalue = len(q)-1
    start = 0
    end = len(q)
    times = end*end-end-1

    while True:
        total = 0
        for i in range(start,end):
            x = q[i]
            total = total+x
            all.append(total)
        end+=-1
        if start == endvalue and end == endvalue:
            break
        elif start == end:
            end = len(q)
            start+=1
    print(all)










s = 'abccddde'

uniform(s)






