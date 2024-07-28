




# Queens on the Board
# https://www.hackerrank.com/challenges/queens-on-board/problem


def newQueenPlacement(board, rn,cn):

    for r in range(0,rn):
        for c in range(0,cn):



def queensBoard(mainBoard,rn,cn):

    # Starting Position
    for r in range(0,rn):
        for c in range(0,cn):
            if mainBoard[r][c] == '#':
                pass
            else:
                newBoard = mainBoard[::]
                for numq in range(0,rn*cn):
                    newBoard[r][c] = 'Q'











t = int(input())
n,m = map(int, input().split(' '))


q = []

for i in range(n):
    j = input()
    r = []
    for i in j:
        r.append(i)
    q.append(r)



print(q)












