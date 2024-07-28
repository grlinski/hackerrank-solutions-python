
# HR Lisa's Workbook
# https://www.hackerrank.com/challenges/lisa-workbook/problem





"""

Problem is special if its index within a chapter is the same as the page it is located on

Workbook Layout
n chapters 1 to n
i'th chapter has arr[i] problems from 1 to arr[i]

Each page can hold up to k problems
Only a chapters last page of exercises may contain fewer than k problems.


Each new chapter starts on a new page
Page numbers start at index 1










"""


n,k = map(int, input().split(' '))

q = list(map(int, input().strip().split(' ')))


q.append(None)
ans = 0
index = 0
a = q[index]
fp = 1
lp = fp+k-1


page = 1
# I've been tracking the index, not the page.

while True:

    #print(index+1,fp,lp,page)

    if page >= fp and page <=lp and page <= q[index]:

        ans+=1
        #print('A', ans)


    a-=k
    if a <=0:
        index+=1
        a = q[index]
        fp = 1
        lp = fp + k - 1
    else:
        fp += k
        lp += k

    if a == None:
        break
    page+=1





print(ans)








