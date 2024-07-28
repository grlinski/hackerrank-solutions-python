

# https://www.hackerrank.com/challenges/climbing-the-leaderboard/problem

# Climbing the Leaderboard Mk2, Technically Mark 5
# Been a while since I tried this challenge.



"""


Input
Number of Players
Their Scores
Number of Levels Played By Alice
Her Scores

Out Her Rank



Store how many ranks alice has passed and if the score is equal

"""





n = int(input().strip())
score = list(map(int, input().strip().split(' ')))
m = int(input().strip())
alice = list(map(int, input().strip().split(' ')))


# Score Compression
s = []
s2 = []
h=[]
prev = score[0]
t = 1

for i in range(1,len(score)):

    if score[i] == prev:
        t+=1
    else:
        #h.append(prev)
        #h.append(t)
        #t = 1
        #s2.append(h)

        s.append(prev)





        h = []
    prev = score[i]


# House Keeping
#h.append(prev)
#h.append(t)
#s2.append(h)

s.append(prev)








# Alice starts at the lowest rank, which is +1 the number of rankings
rank = len(s)+1
# Score Position, where we are in the compressed score list
sp = len(s)-1

breaker = alice[0]

ap = 0

while ap < len(alice):
    a = alice[ap]


    if sp == 0:
        #print('end')

        if a > sp:
            rank-=1
        for i in range(len(alice)-ap):
            print(rank)
        break



    if a == s[sp]:

        rank-=1
        print(rank)
        ap+=1
    elif a < s[sp]:
        print(rank)
        ap+=1
    elif a > s[sp]:
        rank-=1
        sp-=1


print(s[::-1])
print(alice)














