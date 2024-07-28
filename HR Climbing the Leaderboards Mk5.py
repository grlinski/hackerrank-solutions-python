

# Climbing the Leaderboards Mk5
# https://www.hackerrank.com/challenges/climbing-the-leaderboard/problem



nscores = int(input())

sscores = set(map(int, input().strip().split(' ')))

nalice = int(input())
alice = list(map(int, input().strip().split(' ')))

passed = []

scores = list(sscores)
scores.sort()
nplayers = (len(scores))+1

i = 0
j = 0
counter = 0

while i < len(alice) and j < len(scores):
    apos = alice[i]
    spos = scores[j]

    if apos < spos:
        print(nplayers)
        i+=1
    elif spos < apos:
        nplayers -=1
        j+=1
    elif spos == apos:
        nplayers -= 1
        #print(nplayers)
        j+=1

    #print(i,j,apos,spos,nplayers)




print(nplayers)








