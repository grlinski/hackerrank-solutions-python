


def restaurant(l, b):
    size = l*b

    while l != b:
        if l > b:
            l = l - b
        else:
            b = b - l

    return size//(l*l)




l,b = map(int, input().split(' '))

print(restaurant(l,b))








