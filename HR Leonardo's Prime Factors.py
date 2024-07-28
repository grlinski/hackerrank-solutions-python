

# Leonardo's Prime Factors
# https://www.hackerrank.com/challenges/leonardo-and-prime/problem

import math,datetime

start = datetime.datetime.now()

def prime_number_gen(items):
    list_of_primes = [2,3,5]
    # 2 and 3 added since they are a pain in the ass
    counter = 3
    number = 7
    prime = True
    # Main Loop for Prime Gen
    # Goes until our counter of primes hits items
    while counter != items:

        prime = True
        # Quick check if prime
        # The number has to be either 6n+1 or 6n-1,
        # Note I had a problem before with using or instead of and.
        # It only needs to be one or the other, not nessicarily both.
        if (number+1)%6 != 0 and (number-1)%6 != 0:
            prime = False

        elif number % 2 == 0 or number % 3 == 0 or number % 5 == 0:
            prime = False
            # If all those fail check if it is divisible by any of the primes in the list
        else:
            # If the potential divisor is greater than the square root of the number it ends
            # This is one of the most important parts
            # Makes it much more efficient
            upto = int(math.sqrt(number))
            for i in range(2,len(list_of_primes)):
                if i > upto:
                    break
                if number%list_of_primes[i] == 0:
                    prime = False
                    break
        if prime == True:
            list_of_primes.append(number)
            counter += 1
            if len(list_of_primes)%10000 == 0:
                pass
                #print(counter)



        number+=1
    return list_of_primes



def leoprime(n,p):
    count = 0
    pp = 0
    np = 0
    ans = []
    total = 1
    ender = int(math.sqrt(n[-1]))

    while True:
        x = n[np]
        y = p[pp]
        total = total*y


        if total > x:
            ans.append(count)
            np+=1
        if total > ender:
            break
        count += 1



        pp+=1
    return ans





"""
Max amount of prime factors inclusive and under the number

"""




n = int(input())
q = []
for i in range(0,n):
    j = int(input())
    q.append(j)


maxi = int(math.sqrt(q[-1]))
print(maxi)
primes = prime_number_gen(maxi)


print(leoprime(q,primes))




end = datetime.datetime.now()

print(end-start)



































