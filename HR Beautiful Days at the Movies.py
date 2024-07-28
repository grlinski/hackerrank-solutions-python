

# Beautiful Days at the Movies
# https://www.hackerrank.com/challenges/beautiful-days-at-the-movies/problem



def beautifulDays(i, j, k):
    count = 0
    for i in range(i,j+1):
        s = str(i)
        r = s[::-1]
        x = int(r)
        y = abs(i-x)%k
        if y == 0:
            count+=1
    return count





beautifulDays(20,23,6)













