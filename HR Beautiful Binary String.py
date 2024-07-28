
# Beautiful Binary String
# https://www.hackerrank.com/challenges/beautiful-binary-string/problem

def beautifulBinaryString(b):

    count=0
    for i in range(2,len(b)-1):
        if b[i-2] == '0' and b[i-1] == '1' and b[i] == '0':
            b[i-2] == '1'
            count+=1
    return count





b = '0100101010'

print(beautifulBinaryString(b))










