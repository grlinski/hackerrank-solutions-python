

# Mars Exploration

# https://www.hackerrank.com/challenges/mars-exploration/problem



def marsExploration(s):
    counter = 0
    times = 1
    for i in s:
        if (times%3 == 2 and i == 'O'):
            pass
        elif (times%3 == 1 or times%3 == 0) and i == "S":
            pass
        else:
            counter+=1

        times+=1

    return counter






s = input()
print(marsExploration(s))







