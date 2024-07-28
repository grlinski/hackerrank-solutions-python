

import math,re,cmath

def distance(x1,y1,x2,y2):
    dis = ((abs(x1-x2)**2)+(abs(y1-y2)**2))**(1/2)
    return dis

# Regex
digi = re.compile(r'\d+')
x = '1+2j'
q = digi.findall(x)
minplus = x[1]

for i in range(0,len(q)):
    if i == '':
        del(q[i])
a = int(q[0])
b = int(q[1])




dis = (distance(a,b,0,0))

cosy = math.acos(a/dis)
print(dis)

if minplus == '-':
    cosy = cosy*-1
print(cosy)




















