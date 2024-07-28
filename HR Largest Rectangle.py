

# Largest Rectangle
# https://www.hackerrank.com/challenges/largest-rectangle/problem



def largestRectangle(h):

    ans = 0
    skip = False

    q = []




    for i in range(0,len(h)):
        start = h[i]
        # Total Buildings, always at least one.
        tb = 1

        print('Number', i + 1)
        print('Building', start)



        if i == 0:
            left = 0
            right = h[i+1]
        elif i == len(h)-1:
            right = 0
            left = h[i-1]
        else:
            right = h[i + 1]
            left = h[i - 1]


        # Rectangle Sizes
        # The first case is if the start building is taller than it's left and right
        if start > right and start < left:
            rect = start

        # Going Right
        if start <= right:
            for j in range(i+1, len(h)):
                cb = h[j]
                if cb < start:
                    break
                elif cb >= start:
                    tb += 1
                    print(cb)

        # Going Left
        if start <= right:
            for j in range(i-1, -1,-1):
                cb = h[j]
                if cb < start:
                    break
                elif cb >= start:
                    tb += 1
                    print(cb)

        rect = start * tb



        print('Count',tb)
        print('Rect',rect)

        ans = max(ans,rect)

    return ans

















n = int(input())
h = list(map(int, input().strip().split(' ')))


print(largestRectangle(h))










