


# https://www.hackerrank.com/challenges/ctci-ransom-note/problem?h_l=playlist&slugs%5B%5D=interview&slugs%5B%5D=interview-preparation-kit&slugs%5B%5D=dictionaries-hashmaps
# Ransom Note


# It is recommended to use collections
# I'm going to try to create two dictionaries and compare them at the end
# Works, much faster than comparing lists




def checkMagazine(magazine, note):
    mdic = {}
    ndic = {}

    for i in magazine:
        if i in mdic:
            mdic[i]+=1
        else:
            mdic[i]=1

    for i in note:
        try:
            x = mdic[i]
            mdic[i] = mdic[i] -1
            #print(x)
            if x == 0:
                print(i)
                print(mdic[i])
                return 'No'
        except:
            return 'No'

    return 'Yes'









m,n = map(int, input().split(' '))
mag = input().split()
note = input().split()

print(checkMagazine(mag, note))






















