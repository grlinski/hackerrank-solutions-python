






# HR Pythagorean Triple
# https://www.hackerrank.com/challenges/pythagorean-triple/problem

"""
One side must be even

a = u2-v2
b = uv
c = u2+v2

a = 2v+1
b = 2v2 +2v
c = 2v2+2v+1


Solve for v in either b or c formula




Where u and v are relatively prime intergers, not both odd




"""







import math



side1 = int(input())




def triple_find(x):

    # Possible Side
    # If x is the smaller side
    n1 = int((side1 - 1) / 2)

    large = int(2*(n1**2) +2*n1)
    correct = False

    correct,a1,b1,c1 = squarer(x,large)
    if correct == True:
        return a1,b1,c1

    # Possible Side
    # If x is the larger side

    n2 = 0
    n3 = 0
    n2,n3 = qsolve(2,2,-x)

    s2 = int((2*n2)+1)
    s3 = int((2*n3)+1)

    correct, a1, b1, c1 = squarer(s2, x)
    if correct == True:
        return a1, b1, c1

    correct, a1, b1, c1 = squarer(s3, x)
    if correct == True:
        return a1, b1, c1



def qsolve(a,b,c):
    ans1 = 0
    ans2 = 0

    try:
        minus = ((-b)-math.sqrt((b**2)-(4*a*c)))/(2*a)
        ans1 = minus
    except:
        pass

    try:
        plus = ((-b)+math.sqrt((b**2)-(4*a*c)))/(2*a)
        ans2 = plus
    except:
        pass

    return ans1,ans2


def squarer(sml,lrg):

    #print(sml,lrg)
    sml = abs(sml)
    lrg = abs(lrg)

    hyp = math.sqrt(sml**2+lrg**2)
    hyp = int(hyp)
    if (hyp**2) == (sml**2 + lrg**2):
        return True, int(sml),int(lrg),int(hyp)
    else:
        return False, sml, lrg, hyp




print(triple_find(side1))


"""
a = 12
b = -24
c = 9

a = 2
b = 2
c = -12
"""

# 0 = 2x2 +2x - 8
"""



# If side1 is the smaller side
# Possible n value
n = (side1-1)/2


# Second side
side2 = (2*n**2 +2*n)


hyp = math.sqrt(side1**2 + side2**2)
print(side1,int(side2),int(hyp))



# If side1 if the larger side


(m2 +n2)2 = (m2 - n2)2 + (2mn)2

m2 +n2 * m2 + n2

h
m4 2m2n2 + n4


Small Side
(m2 - n2)2
(m2 - n2) * (m2 - n2)
m4 -m2n2 -m2n2 + n4

m4 - 2m2n2 + n4



Large Side
4m2n2

# Expanded Equation
m4 + 2m2n2 + n4 = m4 - 2m2n2 + n4 + 4m2n2

# Simplified
2m2n2 = 4m2n2 - 2m2n2


2m2n2 = 2m2n2
m2n2 = m2n2
m2n2/m2 = n2




b = 2v2 + 2v
b/2 = v2+v

0 = 2x2 +2x - 8
"""












