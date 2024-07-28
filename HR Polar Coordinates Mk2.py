# https://www.hackerrank.com/challenges/polar-coordinates/problem
import math, cmath

a = input()
# Convert the two numbers into ints
x = ""
y = ""
switch = 0
for i in a:
    if switch == 0 and i !="+":
        x = x+i
    elif i == "+":
        switch = 1
    elif switch == 1 and i != "j":
        y = y+i
    elif i == "j":
        break
x = int(x)
y = int(y)

r = math.sqrt((x**2+y**2))

print(r)
print(cmath.phase(complex(x,y)))





