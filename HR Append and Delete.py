
# Append and Delete
# https://www.hackerrank.com/challenges/append-and-delete/problem




def appendAndDelete(s, t, k):
    # Get s to t in k steps
    lens = len(s)
    lent = len(t)
    lenk = len(k)

    # Check different cases

    # Case 1, not enough steps
    if abs(lens-lent) > lenk:
        return 'NO'







s = 'abbbabab'
t = 'aba'
k = 3









