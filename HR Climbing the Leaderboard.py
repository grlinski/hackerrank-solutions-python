
# https://www.hackerrank.com/challenges/climbing-the-leaderboard/problem

# Climbing the Leaderboard

"""


Input
Number of Players
Their Scores
Number of Levels Played By Alice
Her Scores

Out Her Rank


timed out?
Too Slow




"""



def climbingLeaderboard(scores, alice):
    scores.sort()
    q = []
    for i in scores:
        if i not in q:
            q.append(i)
    amount = len(q)

    j = 0
    index = 0
    change = 0


    # Two Cases Either the Score is in the Score List or it isn't
    for i in alice:
        #print("A Score: ", i)
        j = j+change

        count = 0
        # Is In, note that the ranks don't increase
        if i in q:
            for j in q:
                if i == j:
                    print(amount-count)
                    break
                else:
                    count+=1
        # Not in, number of ranks increases by one
        else:
            # Top Score
            if i > q[-1]:
                print(1)
            # Lowest Score
            elif i < q[0]:
                print(amount+1)
            # Middle Score, Find Where
            else:
                for j in range(0,len(q)):
                    if i > q[j]:
                        count+=1
                        change+=1
                    else:
                        print(amount-count+1)
                        break









n = int(input().strip())
scores = list(map(int, input().strip().split(' ')))
m = int(input().strip())
alice = list(map(int, input().strip().split(' ')))

climbingLeaderboard(scores,alice)





"""

8
8 7 6 5 4 3 2 1
8
0 1 2 2 4 4 7 9


3
30 20 10
2
20 20




"""








