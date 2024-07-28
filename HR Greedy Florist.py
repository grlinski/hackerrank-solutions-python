
# Greedy Florist
# https://www.hackerrank.com/challenges/greedy-florist/problem?h_l=interview&playlist_slugs%5B%5D%5B%5D=interview-preparation-kit&playlist_slugs%5B%5D%5B%5D=greedy-algorithms


"""

Price of each flower * number of that customer's previously purchased flowers + 1

First flower = (0+1)*original price
Second = (1+1)*original price
Third = (2+1)*op

Given size of group of friends and number of flower they want to buy
Determine min cost to purchase flowers
n,k
flowers,friends
flower prices


Things I learned
Basically repeats the message to read the question
Made it much easier than a quick glance.






"""

#flowers,friends
n,k  = map(int, input().split(' '))

fp = list(map(int, input().strip().split(' ')))
fp.sort(reverse =True)

total = 0
counter = 0
repeats = 0

for i in range(0,len(fp)):
    op = fp[i]
    price = op*(1+repeats)
    total+=price

    counter+=1
    #print(op,price,repeats)


    if counter == k:
        counter = 0
        repeats+=1

print(total)











