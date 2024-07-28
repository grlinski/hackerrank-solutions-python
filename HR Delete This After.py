"""
Just Used to Generate another file



"""
words = []
s = input()
newS = ''
for i in s:
    if i =='\'':
        pass
    elif i == ',':
        pass
    elif i == ' ':
        words.append(newS)
        newS = ''
    else:
        newS+=i
words.append(newS)
total = 0
for i in words:
    print(i)
    total+=1

print(total)


