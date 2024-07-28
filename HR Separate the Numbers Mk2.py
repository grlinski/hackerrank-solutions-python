


def numberizer(s,digits):
    useAble = True
    num1 = int(s[0:digits])
    s = s[digits:]
    numbers = [num1]
    if len(str(num1+1)) > len(str(num1)):
        digits+=1
    while True:
        if s[0] == '0':
            useAble = False
            break
        curNum =int(s[:digits])
        s = s[digits:]
        if len(str(curNum + 1)) > len(str(curNum)):
            digits += 1
        numbers.append(curNum)
        if len(s) == 0:
            break

    if useAble == True:
        for i in range(0,len(numbers)-1):
            cur = numbers[i]
            next = numbers[i+1]
            if cur+1 == next:
                pass
            else:
                useAble = False

    if useAble == True and len(numbers)>1:
        print('YES',numbers[0])
        return True
    else:
        return False




n = int(input())

for i in range(n):
    s = input()
    maxDigits = len(s)//2
    answer = False
    for d in range(1,maxDigits+1):
        answer = numberizer(s,d)
        if answer == True:
            break
    if answer==False:
        print('NO')




"""

99100101


"""



