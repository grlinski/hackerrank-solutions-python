import math

if __name__ == '__main__':
    students = []
    marks = []
    diction = {}


    def second_lowest(x):
        # Note Need to Set Both Lowest and Second to very high values
        # Otherwise this won't work

        # Problem with the ordering of Numbers
        lowest = x[0]
        second = x[0]
        third = 10000
        for i in x:
            lowest = min(lowest, i)
            if i != lowest and i < second:
                second = i
            elif i != lowest and i > second and i < third:
                third = i
        if lowest == second:
            return third
        return second


    for _ in range(int(input())):
        name = input()
        score = float(input())
        diction[score] = name
        students.append(name)
        marks.append(score)
    ans = []

    second = second_lowest(marks)

    for i in range(0, len(marks)):
        if marks[i] == second:
            ans.append(students[i])
    ans.sort()
    for i in ans:
        print(i)

        # print(lowest,secondlow)





