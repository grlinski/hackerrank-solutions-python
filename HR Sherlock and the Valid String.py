


# Sherlock and the Valid String
# https://www.hackerrank.com/challenges/sherlock-and-valid-string/problem?h_l=interview&playlist_slugs%5B%5D=interview-preparation-kit&playlist_slugs%5B%5D=strings



"""
Passes 14/20 cases
Possibly doesn't work with low amounts of letters?

Ex
abbac
Should be yes, as if we remove c, then the remaining letters a and b are equal.


"""






s = input()
q = [0]*26
total=0
for i in s:
    x = ord(i)-97
    q[x]+=1
    total+=1

count = 0
for i in q:
    if i!=0:
        count+=1


# All counts = 1 or 0, checker1
# Only 1 count of 1.

# Checker2 is causing problems in cases 6 and 19
# Checker2 is there to see if there is a single letter count of 1, and all the rest are equal.

# Checker3 is for non-removals.
# Check if all the values are the same or 0

checker1 = True
checker2 = 0
checker3 = True
checker4 = False
maxi = 0
mini = 10000000

c2h = max(q)

# Checker2 problem, I only checked if there is a single case of 1.
# Need to also see if everything else is equal.

counter = q.count(1)




for i in q:
    if i!= 0  and i!= 1:
        checker1 = False
        if c2h!= i:
            checker2 = 1000




    if i==1:
        checker2+=1



    if i!=0:
        maxi = max(maxi, i)
        mini = min(mini,i)
        if maxi!=mini:
            checker3 = False


freq =[]
for v in range(1,max(q)+1):
    x = q.count(v)
    if x!=0:
        freq.append(x)
print(freq)




if count == 1:
    print('YES')
#elif (total-1)%count==0:




 #   print('YES0')
elif checker1 == True:
    print('YES1')
elif checker2 == 1:
    print('YES2')
elif checker3 == True:
    print('YES3')
else:
    print('NO')


print(count)
print(q)
print(total)


"""

Yeses
abcdefghhgfedecba
8
17

Nos
aabbccddeefghi
9
14


"""






