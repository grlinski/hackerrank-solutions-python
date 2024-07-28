

# ginsortS
# https://www.hackerrank.com/challenges/ginorts/problem


def sorter(x):
    lower = []
    upper = []
    odd = []
    even = []

    for i in x:
        if i.isupper():
            upper.append(i)
        elif i.islower():
            lower.append(i)
        else:
            chk = int(i)
            if chk%2 == 0:
                even.append(i)
            else:
                odd.append(i)

    lower.sort()
    upper.sort()
    odd.sort()
    even.sort()



    s1= ''
    s2 = ''
    s3 = ''
    s4 = ''

    s1 = s1.join(lower)
    s2 = s2.join(upper)
    s3 = s3.join(odd)
    s4 = s4.join(even)

    return(s1+s2+s3+s4)











x = input()
print(sorter(x))


"""
Lower case letters ahead of uppercase
Uppercase ahead of digits
Odd digits ahead of even



"""








