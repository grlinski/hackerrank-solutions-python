

# The Minion Game
# https://www.hackerrank.com/challenges/the-minion-game/problem


# This Code Works but takes too long
# However it is a pretty good coding example so I'm keeping it



VOWELS = "AEIOUaeiou"

def minion_game(string):
    q = []
    end = len(string)
    start = 0
    stuart = 0
    kevin = 0
    ns= ""
    for k in range(start,end):
        for i in range(start,end):
            ns = ""
            for j in range(start,end):
                ns = ns+string[j]
            q.append(ns)
            if ns[0] in VOWELS:
                kevin+=1
            else:
                stuart+=1
            end-=1
        end = len(string)
        start+=1
    #print(q)
    #print(stuart)
    if stuart > kevin:
        print('Stuart',stuart)
    elif kevin > stuart:
        print('Kevin',kevin)
    else:
        print('Draw')












minion_game("BANANA")




















