

# Left Rotation
# https://www.hackerrank.com/challenges/array-left-rotation/problem


nums,rot = map(int, input().split(' '))
a = list(map(int, input().rstrip().split()))

print(a)

head = a[:rot]
tail = a[rot:]


nu = tail+head
for i in nu:
    print(i,end=' ')















