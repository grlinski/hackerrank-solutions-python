

# https://www.hackerrank.com/challenges/climbing-the-leaderboard/problem

import random,datetime


def data_gen():
    scores = []
    alice = []
    aa = []
    n = random.randint(2,100000)
    m = random.randint(2,100000)
    for i in range(0,n):
        x = random.randint(0,1000000000)
        scores.append(x)
    scores.sort()
    for i in range(0,m):
        x = random.randint(0,1000000000)
        aa.append(x)
    aa.sort()
    for i in range(len(aa)-1,0,-1):
        alice.append(aa[i])


    return scores,alice




def climbingLeaderBoard(scores,alice):

    # Scores descending
    # Alice ascending
    total = len(scores)-1
    movement = 0
    spos = total-1
    apos = 0

    # These are used later to see how many unique values there are
    ranks = []
    values = 0


    a = alice[apos]
    s = scores[spos]

    first = scores[0]
    last = scores[-1]

    while apos != len(alice)-1:


        # Two Cases
        # If ascore < the lowest score
        if a <= first:
            apos+=1
            print(total)
        elif a >= last:
            apos+=1
            print(1)


        elif a > s:
            apos+=1
            spos=-1
            movement+=1
            print(total-movement)
        elif a < s:
            apos+=1
            print(total-movement)
        elif a == s:
            apos+=1
            print(total-movement)

        a = alice[apos]
        s = scores[spos]

















"""
Sample Input
7
scores= [100, 100, 50, 40, 40, 20, 10]
4
alice = [5, 25, 50, 120]


"""






x = [100, 100, 50, 40, 40, 20, 10]
y = [5, 25, 50, 120]








#x,y = data_gen()
climbingLeaderBoard(x,y)
print(x[-1],y[-1])










