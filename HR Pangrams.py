


# Pangrams
# https://www.hackerrank.com/challenges/pangrams/problem



def pangram(s):
    pg = []
    for i in range(0,26):
        pg.append(0)

    for i in s:
        x = ord(i)
        if x >64 and x<91:
            x = x-65
            pg[x]+=1
        elif x >96 and x<123:
            x = x-97
            pg[x] +=1

    for i in range(0,26):
        if pg[i] == 0:
            return 'not pangram'

    print(pg)
    return 'pangram'







s = input()
print(pangram(s))

















