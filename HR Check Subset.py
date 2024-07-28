





t = int(input())


for i in range(t):
    pa = int(input())
    a = set(map(int, input().split()))
    pb = int(input())
    b = set(map(int, input().split()))

    c = len(a&b)
    if c == pa:
        print('True')
    else:
        print("False")










