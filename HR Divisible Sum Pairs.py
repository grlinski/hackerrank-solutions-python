
#HackerRank Divisible Sum Pairs
#https://www.hackerrank.com/challenges/divisible-sum-pairs


# Splits the first two values and then converts into int
a,b = input().split()
amount = int(a)
divisor = int(b)
counter = 0

# Creates an Array from a string of numbers
ar = list(map(int, input().strip().split(' ')))


#Adds together all numbers in the array with those higher than it
# Then checks if the sum is divisible by the divisor(k)
for i in range(0, amount):
    for j in range(i+1, amount):
        if (ar[i]+ar[j])%divisor == 0:
            counter=counter+1
        print(ar[i],ar[j],counter)

print(counter)
print(amount)
print(divisor)

"""
Sample Data


6 3
1 3 2 6 1 2


"""



