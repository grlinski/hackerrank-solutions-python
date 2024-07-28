
"""
items = int(input())
doors = list(map(int, input().strip().split(' ')))


"""

items = 10
doors1 = [0, 1, 1, 0, 1, 1, 1, 1, 0, 0]
doors2 = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
doors3 = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1]
doors4 = [0, 1, 1, 0, 1, 1, 1, 1, 0, 0]
doors5 = []


def revisedRussianRoulette(doors):
    miniops = 0
    maxiops = 0
    doors.append(9)
    for i in range(0,len(doors)):
        x = doors[i]
        if x == 9:
            break
        y = doors[i+1]
        if x == 0:
            pass
        elif x == 1 and y == 1:
            maxiops+=2
            miniops+=1
            doors[i+1] = 0
        elif x == 1:
            maxiops +=1
            miniops +=1

    return(miniops,maxiops)


print(revisedRussianRoulette(doors3))
















