




#s = 'aaaaaa'
s = 'aaaa'


d = {}

first = 0
second = 0
third = 0


for i in s:
    if i not in d:
        d[i] = 1
    else:
        d[i]+=1

letter = []
number = []
for i in d:
    letter.append(i)
    number.append(d[i])



rev = sorted(number)
first = rev[-1]
second = rev[-2]
third = rev[-3]



ans1 = []
ans2 = []
ans3 = []

for i in range(0,len(number)):
    if number[i] == first:
        temp = []
        t = letter[i]
        u = number[i]
        temp.append(t)
        temp.append(u)
        ans1.append(temp)
    if number[i] == second:
        temp = []
        t = letter[i]
        u = number[i]
        temp.append(t)
        temp.append(u)
        ans2.append(temp)
    if number[i] == third:
        temp = []
        t = letter[i]
        u = number[i]
        temp.append(t)
        temp.append(u)
        ans3.append(temp)

ans1.sort()
ans2.sort()
ans3.sort()


times = 3
while times > 1:

    for i in ans1:
        print(i[0],i[1])
        times-=1
        if times <1:
            break
    if times < 1:
        break

    for i in ans2:
        print(i[0],i[1])
        times-=1
        if times <1:
            break
    if times < 1:
        break

    for i in ans3:
        print(i[0],i[1])
        times-=1
        if times <1:
            break



















