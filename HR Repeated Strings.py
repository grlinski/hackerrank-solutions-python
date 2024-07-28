

# https://www.hackerrank.com/challenges/repeated-string/problem
"""
Given a string s
And a number n
Assuming the string repeats infinitely how many times does 'a' appear with in the first nth of the string

Example
s = 'aba'
n = 5
So the string would go on like
ababababababababa
So within the first 5 spots there are 3 a's




"""

n = 1000000000
s = 'aba'
x = ""

divisors = []
ender = 1

while ender == 1:
    for r in range(2,100):
        check = n%r
        if n/r == 1:
            ender = 0
            break
        if check == 0:
            divisors.append(r)
            n = n/r
            r = 2
            print(n)


print(divisors)
counter = len(divisors)-1
for i in range(0,len(divisors)):
    n = n*divisors[counter]
    counter -=1
print(n)


"""

Continually divide by every number under say 20, or maybe 100
ex
n
n/2
(n/2)/3
(n/2)/3)/21
And so on
Until the number is perfectly divided
Now we don't want it perfectly divided per se
But let's say we end up with 17
So the loop will stop when we divide 17 by 17
Then count how many times a appears in 17
Then multiply that number by all the divisors in the reverse order.








"""










