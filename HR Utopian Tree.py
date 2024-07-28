

# Uptopian Tree
# https://www.hackerrank.com/challenges/utopian-tree/problem






def utopianTree(n):
    init = 1
    double = True
    for i in range(0,n):
        if double == True:
            init = init*2
            double = False
        else:
            init = init+1
            double = True
    return init





q = 4

print(utopianTree(q))





