

# The Minion Game
# https://www.hackerrank.com/challenges/the-minion-game/problem


# This is less fun than Mark 1, but does what is needed way faster
# Uses an math algorithm rather than generating every substring


VOWELS = "AEIOUaeiou"

def minion_game(string):
    total = len(string)
    stuart = 0
    kevin = 0

    for i in string:
        if i in VOWELS:
            kevin +=total
        else:
            stuart+=total
        total-=1
    if kevin == stuart:
        print('Draw')
    elif kevin > stuart:
        print('Kevin',kevin)
    else:
        print('Stuart',stuart)















minion_game("BANANA")




















