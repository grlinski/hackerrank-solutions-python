

# CamelCase
# https://www.hackerrank.com/challenges/camelcase/problem



def camelcase(s):
    counter = 1
    for i in s:
        if i.isupper() == True:
            counter+=1
    return counter









s = input()
camelcase(s)





