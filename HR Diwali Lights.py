
# HR Diwali Lights
# https://www.hackerrank.com/challenges/diwali-lights/problem



def lights(n):

    if n == 1:
        return 1

    count = (2**n)-1
    return count%100000



x = int(input())

print(lights(x))















