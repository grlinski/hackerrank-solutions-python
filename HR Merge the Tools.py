
# Merge the Tools

# https://www.hackerrank.com/challenges/merge-the-tools/problem



def merge_the_tools(string, k):
    q = []
    end = 0
    for i in range(0,len(string),k):
        ns = ""
        end = end+k
        for j in range(i,end):
            ns = ns+string[j]
        q.append(ns)

    for string2 in q:
        ns = ""
        for i in string2:
            if i in ns:
                pass
            else:
                ns = ns+i
        print(ns)




merge_the_tools("AABCAAADA",3)













