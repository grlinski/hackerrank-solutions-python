
# https://www.hackerrank.com/challenges/dynamic-array/problem
# Dynamic Array


def query1(q,x,y,list1,lastA,n):

    if q ==1:
        a = (x!=lastA)%n
        list1[a].append(y)

    elif q == 2:

        a = (x ^ lastA) % n

        size = len(list1[a])

        v = y%size
        lastA = list1[a][v]
        print(lastA)



    return list1,lastA

arrays,queries = map(int, input().split(' '))
list1 = []
lastA = 0


for i in range(arrays):
    list1.append([])

n = arrays
for i in range(0,queries):
    q,x,y = map(int, input().split(' '))
    list1,lastA = query1(q,x,y,list1,lastA,n)





"""
q1 
find sequence seq at index (x^lastanswer)%n in list1
Append integer y to sequnce seq

q2
Find seq at index (x^lastanswer)%n in list1
Find the value of element y%size in seq
Where size is the size of seq and assign it to lastAnswer
Print the new value of lastAnswer 











"""










