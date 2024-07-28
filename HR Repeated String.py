
# Reapeated String
# https://www.hackerrank.com/challenges/repeated-string/problem


def repeatedString(s,n):
    # Count a's in s:
    acount = 0
    lengther = len(s)

    totala = 0
    for i in s:
        if i == 'a':
            acount += 1
    # Two Simple Cases
    # If no a's return 0 and if only a's return n
    if acount == 0:
        return 0
    if acount == len(s):
        return n

    #

    # This gives us how many a's are in a divisible portion of the number
    # Example if s == 'ab' and n = 5, this will give us the amount of a's up to length of 4
    # Then we have to figure it out for the remainder
    rem = n%lengther
    newlength = n-rem
    percenta = acount/lengther
    totala = newlength*percenta

    # Remainder
    for i in range(0,rem):
        if s[i] == 'a':
            totala+=1

    return(int(totala))






#s = input()
#length = int(input())

# Count a's in s:


s = "aba"
n = 100


print(repeatedString(s,n))

















