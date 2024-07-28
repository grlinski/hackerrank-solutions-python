





# Sherlock Divisors Mk2
# https://www.hackerrank.com/challenges/sherlock-and-divisors/problem

# Create a Dictionary
def add_dict(dict,x,y):
    dict[x].append(y)

    return dict





def divisors(n):

    # Odd?
    if n%2 == 1:
        return 0

    count = 1
    q = []

    for i in range(2,n//2+1,2):
        if n%i == 0:
            count+=1
            q.append(i)
    #q.append(n)
    return count



dicta = {}
x = int(input())
print(divisors(x))


















































