


# Find a String
# https://www.hackerrank.com/challenges/find-a-string/problem



def count_substring(s, ss):
    ns = s
    count = 0
    while ss in ns:
        if ss in ns:
            count+=1
            q = ns.find(ss)
            ns = ns[0:q]+ns[q+1:]
    return count



s = 'ABCDCDC'
ss = 'CDC'

print(count_substring(s,ss))














