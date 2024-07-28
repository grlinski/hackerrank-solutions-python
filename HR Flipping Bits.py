

# HR Flipping Bits

#x = int(input())
x = 2147483647


b1 = bin(x)
b2 = str(b1[2:])
print(b2)
print(len(b2))

for i in range(32-len(b2)):
    b2 = '0'+b2
b3 =''
for i in b2:
    if i=='0':
        b3 = b3+'1'
    else:
        b3 = b3+'0'

y = int(b3,2)

print(y)








