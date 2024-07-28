
import requests


def balanced(x):
    # If odd amount cannot be correct bracketing
    #print(x)

    start = '({[<'
    try:
        ender =  x[-1]
        if ender in start:
            return 'NO'
    except:
        pass

    if x == 'NO':
        return 'NO'
    if len(x)%2 == 1:
        return 'NO'
    if len(x) == 0:
        return 'YES'


    # The basics of this are to go through until we hit an end bracket.
    # The preceding bracket must be a start bracket, otherwise return False
    # If correct delete both items and then send it through the function again.

    for i in range(1,len(x)):
        a = x[i]
        b = x[i-1]
        if (a == ')'):
            if b == '(':
                x = x[:i-1]+x[i+1:]
                return balanced(x)
            else:
                return 'NO'

        if (a == '}'):
            if b == '{':
                x = x[:i-1]+x[i+1:]
                return balanced(x)
            else:
                return 'NO'

        if (a == ']'):
            if b == '[':
                x = x[:i-1]+x[i+1:]
                return balanced(x)
            else:
                return 'NO'


        if (a == '>'):
            if b == '<':
                x = x[:i-1]+x[i+1:]
                return balanced(x)
            else:
                return 'NO'











t = int(input())
ans = []
for i in range(t):
    x = input()
    print(balanced(x))

















