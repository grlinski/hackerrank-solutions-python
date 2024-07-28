


# https://www.hackerrank.com/challenges/most-commons/problem
#  Company Logo



#x = input()

x = 'szrmtbttyyaymadobvwniwmozojggfbtswdiocewnqsjrkimhovimghixqryqgzhgbakpncwupcadwvglmupbexijimonxdowqsjinqzytkooacwkchatuwpsoxwvgrrejkukcvyzbkfnzfvrthmtfvmbppkdebswfpspxnelhqnjlgntqzsprmhcnuomrvuyolvzlni'


let = [0]*26

for i in x:
    y = ord(i)
    let[y-97]+=1


#print(ord('z'))

for i in range(0,26):
    let[i] =  str(let[i])+chr(i+97)

#print(let)
let.sort(reverse=True)

s = sorted(let, key = lambda x: (int(x[:-1]), 100-ord(x[-1])),reverse=True)

#print(s)


for i in range(0,3):
    x = s[i]
    num = x[:-1]
    char = x[-1]
    print(char,num)











