

# Leonardo's Prime Factors
# https://www.hackerrank.com/challenges/leonardo-and-prime/problem

"""
Given n = number of queries
then every other number is an integer


Find out how many prime numbers that number is divisble by.


Note!!!
I misread the question, basically it's asking for a number under a given number that is the most divisible by primes
Then return how many primes it is divisible by.

I've mostly gotten the code to work at least for checking a single number and returning how many primes it is divisible by.
Now just iterate through a whole range of numbers.



"""


def primechecker(x):
    prime = 0
    for i in range(2,int(x/2+1)):
        prime = 1
        if x%i == 0:
            prime = 0
            break
    return prime



def prime_factors(x):
    counter = 0
    q = 0
    for i in range(2,int(x/2+1)):
        if x%i == 0:
            q = primechecker(i)
            if q == 1:
                print(i,counter,q)
                counter +=1
    print(counter)









list2 = [2,100,1250,2356,3023]

a = 210
# 210 is divisible by 2,3,5 and 7 which are primes
#Note my code doesn't really work for 3 or 2, so make contingencies for those numbers
prime_factors(a)

print(primechecker(10))




"""


list1 = []
n = input()

while True:
    line = input()
    if line == '':
        break
    list1.append(line)






"""









