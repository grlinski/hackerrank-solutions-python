
# Caesar Cipher
# https://www.hackerrank.com/challenges/caesar-cipher-1/problem



def caesarCipher(s, k):
    new = ""
    while k >= 26:
        k = k - 26
    for i in s:
        x = ord(i)
        if x >64 and x<91:
            x = x+k
            if x > 90:
                x = x -26
            new = new + chr(x)
        elif x >96 and x<123:
            x = x+k
            if x > 122:
                x = x-26
            new = new+chr(x)
        else:
            new = new+i


    return new





s = input().strip()
k = int(input().strip())
result = caesarCipher(s, k)
print(result)















