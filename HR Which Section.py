

# Which Section
# https://www.hackerrank.com/contests/w38/challenges/which-section


"""
n students
numbered 1 to n

m sections
number 1 to m

Section i needs to have exactly ai students
Students assigned to sections in increasing student number
Meaning the first a1 students will be assigned to section 1
The next a2 students will be assigned to section 2

If you have student number k what section will you be assigned to?

Takes n students
you are student number k
Integer array size
Then the section sizes next line


nka




"""



# Complete the whichSection function below.
def whichSection(n, k, a):
    total = 0
    section = 0
    for i in a:
        section+=1
        total = total+i
        if total >= k:
            return section












