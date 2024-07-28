
# Special Palindrome Again
# https://www.hackerrank.com/challenges/special-palindrome-again/problem?h_l=interview&playlist_slugs%5B%5D=interview-preparation-kit&playlist_slugs%5B%5D=strings

# Note, one rule I missed out on was that all characters need to be the same, except the middle one, if there is one.

"""


So this passes about 2/3rds of the cases
However for some unknown reason my program is overcounting on at least 1 of the unsolved testcases.

On case 2 the output should be
1272919
I'm getting
1272927

So I'm overcounting by 8 and I'm not sure where.






New Problem



aacaa

My solution only counts aacaa, it needs to count aca as well.

Also
acaa
Won't count aca, since it matches front and back.
Need to only match the letter and then count the lower number




ccacacabccacabaaaabbcb
Gives me 42

How many are there actually?


"""

# Printing of all segments
def printSeg(b,m,e,z):
    print(b[0]*int(b[1:])+m[0]*int(m[1:])+e[0]*int(e[1:]),z)


def printSegSame(b,z):
    print(b,z)






#n = input()
s = input()

q = []
r = []
t = 0
t2 = 0



prev = s[0]
prev2 = s[-1]
for i in range(0,len(s)):

    f = s[i]
    rev = s[len(s)-i-1]

    if f == prev:
        t+=1
    elif f!= prev:
        x = prev+str(t)
        q.append(x)
        prev = f
        t = 1


    if rev == prev2:
        t2+=1
    elif rev!= prev2:
        x = prev2+str(t2)
        r.append(x)
        prev2 = rev
        t2 = 1



# House Keeping
x = prev+str(t)
q.append(x)
x = prev2+str(t2)
r.append(x)



#print(q)
#print(r)
#print(r[::-1])

total = 0

counts = {}


pali = []
for i in range(0,len(q)):
    # Beginning, Middle, End
    b = q[i]
    try:
        b = q[i]
        m = q[i+1]
        e = q[i+2]
        if b[0] == e[0] and m[1]=='1':
            total+=min(int(b[1:]),int(e[1:]))
            z = min(int(b[1:]),int(e[1:]))
            #printSeg(b,m,e,z)
    except:
        pass

    # Count individual Segements
    x = int(b[1:])
    z = 0
    for y in range(1,x+1):
        total+=y
        z+=y


    if z in counts:
        counts[z]+=1
    else:
        counts[z]=1


    #printSegSame(b,z)





print(total)
print(counts)
print(q[0:3])




