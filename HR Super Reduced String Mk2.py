
# Super Reduced String
# https://www.hackerrank.com/challenges/reduced-string/problem



s = input()



ns = ''
deleter = True
while deleter == True:

    deleter = False
    ns = ''
    i = 0
    while i < len(s)-1:

        a = s[i]
        b = s[i+1]



        if a == b:
            s = s[:i]+s[i+2:]

            deleter = True
            break
        i+=1



if len(s) == 0:
    print('Empty String')
else:
    print(s)



"""
        
"""




