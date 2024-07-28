

# https://www.hackerrank.com/challenges/kangaroo/problem


def kangaroo(x1, v1, x2, v2):
    count1 = x1
    count2 = x2
    answer = "NO"
    for i in range(0, 100):
        count1 = count1+v1
        count2 = count2+v2
        if count1 == count2:
            answer = "YES"
    return answer













