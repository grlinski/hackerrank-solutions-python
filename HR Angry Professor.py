
# Angry Professor
# https://www.hackerrank.com/challenges/angry-professor/problem



"""


students threshold
arrival times


"""

def angryProfessor(k, a):

    ontime = 0
    for i in a:
        if i <= 0:
            ontime+=1

    print(ontime)
    if ontime >= k:
        return 'NO'
    return 'YES'

k = 3
a = [-1, -3, 4, 2]

#print(angryProfessor(k,a))

k = 2
a = [0, -1, 2, 1]

print(angryProfessor(k,a))





















