

# https://www.hackerrank.com/challenges/word-order/problem
# Word Order

"""

Good example of using a dictionary alongside a list



"""



t = int(input())

words = {}
order = []
count=0

for i in range(t):
    x = input()
    if x in words:
        words[x] +=1
    else:
        words[x] = 1
        order.append(x)
        count+=1
print(count)
for i in order:
    print(words[i],end=' ')


















