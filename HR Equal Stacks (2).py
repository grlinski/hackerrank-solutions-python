

# Hits Recurssion Limit of 1000 times

def equalStacks(h1,h2,h3):


    a = sum(h1)
    b = sum(h2)
    c = sum(h3)

    if a == b and b == c:
        return a
    elif a >= b and a >= c:
        del(h1[0])
        return equalStacks(h1,h2,h3)
    elif b >= a and b >= c:
        del(h2[0])
        return equalStacks(h1,h2,h3)
    else:
        del(h3[0])
        return equalStacks(h1,h2,h3)




x = input().split()

n1 = int(x[0])

n2 = int(x[1])

n3 = int(x[2])

h1 = list(map(int, input().rstrip().split()))

h2 = list(map(int, input().rstrip().split()))

h3 = list(map(int, input().rstrip().split()))


print(h1)






print(equalStacks(h1,h2,h3))










