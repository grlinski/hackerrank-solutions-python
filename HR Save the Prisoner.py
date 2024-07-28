


# Save the Prisoner
# https://www.hackerrank.com/challenges/save-the-prisoner/problem



def saveThePrisoner(n, m, s):
    m = m-1
    if m+s <= n:
        return(m+s)
    else:
        # Go to position 1
        m = m-((n-s))-1
        return(m%n+1)










#print(saveThePrisoner(5,2,2))

#print(saveThePrisoner(5,10,3))
print(saveThePrisoner(7, 19, 2))
print(saveThePrisoner(3, 7, 3))

"""

The last piece is the bad candy
n = number of people
m is the number of sweets/candy
s is the number we start at.



"""



