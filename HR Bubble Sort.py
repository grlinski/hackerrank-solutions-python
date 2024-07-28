



# HR Bubble Sort

# https://www.hackerrank.com/challenges/ctci-bubble-sort/problem?h_l=interview&playlist_slugs%5B%5D=interview-preparation-kit&playlist_slugs%5B%5D=sorting


a = [6,5,4,3,2,1]
#a = [3,2,1]


total=0
i = 0
swaps = True
while swaps == True:
    swaps = False
    for j in range(i,len(a)-1):
        f = a[j]
        s = a[j+1]


        if s < f:
            h = f
            a[j] = a[j+1]
            a[j+1] =h
            total+=1
            swaps = True
            i = 0




print('Array is sorted in',total, 'swaps.')
print('First Element:', a[0])
print('Last Element:', a[-1])










