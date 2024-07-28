
# https://www.hackerrank.com/challenges/climbing-the-leaderboard/problem

# Climbing the Leaderboard Mk2
# Original Too Slow for Mass Data

"""


Input
Number of Players
Their Scores
Number of Levels Played By Alice
Her Scores

Out Her Rank


timed out?
Too Slow

Mk2
Two Things to make it faster
Note that Alice's Scores are in increasing order
The existing scores are in descending order
If we keep an index of where we left off last time and work with these lists I don't need to continually restart at zero

So changes from Mk1
Don't resort into a new list q
Don't sort scores
Change orientation of my sorting, start at the end of scores, -1 and work my way up to the start

??
Easy way to figure out how many rankings there are without sorting?
Maybe store how many non-duplicates I've gone through
Store all the scores in a list


Store how many ranks alice has passed and if the score is equal


"""



def climbingLeaderboard(scores, alice):
    # How many ranks alice has passed
    passed = []
    # If the rank she ends at is equal to another rank
    equal = []
    index = len(scores)-1
    # Ranks is how many ranks have been passed/There are
    rank = 0
    ender = len(alice)
    change = 0
    for numa in alice:
        index = len(scores)-1-change



        for j in range(index,0,-1):

            # Less than The Lowest Score
            # Scores don't increase, Alice does though
            if numa < scores[j] and numa < scores[-1]:
                equal.append(0)
                passed.append(rank)
                print("Lowest Score ", numa, scores[j])

                break
            # If Greater than the Highest Score
            # Index and Alice both increase and Rank
            elif numa > scores[j] and numa > scores[0]:
                rank+=1
                change+=1

                equal.append(0)
                passed.append(rank)
                print("Highest Score ", numa, scores[j])
                break
            # If score and Alice are equal
            # Rank doesn't change, alice changes, index doesn't since the next alice may be the same
            elif numa == scores[j]:
                equal.append(1)
                passed.append(rank)
                print("Equal Score ", numa, scores[j])
                break
            # If score is greater than Alice
            # Index doesn't change, Alice changes
            elif scores[j] > numa:
                equal.append(0)
                passed.append(rank)
                print("Lesser Score ", numa, scores[j])
                break
            # If score is less than Alice:
            # Rank increases, Alice doesn't, Index Does, No appending
            elif scores[j] < numa:
                print("Greater Score ", numa, scores[j])
                rank+=1
                change+=1
            print(index)
        ender-=1
        if ender == 0:
            break

    print(equal)
    print(rank)
    print(passed)
    for i in range(0,len(passed)):
        print(rank-passed[i]+1)



















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


2
10 20 30
2
20 20




"""








