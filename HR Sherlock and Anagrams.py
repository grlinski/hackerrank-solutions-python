

# HR Sherlock and Anagrams
# https://www.hackerrank.com/challenges/sherlock-and-anagrams/problem?h_l=interview&playlist_slugs%5B%5D=interview-preparation-kit&playlist_slugs%5B%5D=dictionaries-hashmaps



def sherlockAndAnagrams(s):
    q = []
    prev = s[0]
    total = 0
    set1 = ()
    set2 = ()

    for i in range(0,len(s)):
        a=''
        for j in range(i,len(s)+1):
            x = (s[i:j])
            if x!='':
                y = stringsort(x)
                q.append(y)


    total = 0
    for i in range(0,len(q)):
        for j in range(1+i,len(q)):
            if q[i] == q[j]:
                #print(q[i],q[j])
                total+=1
    print(total)


def stringsort(x):
    y=[]
    for i in x:
        y.append(i)
    y.sort()
    return y





t = 1
#t = int(input())


for i in range(t):
    #s = input()
    s = 'ifailuhkqqashdjasdhkajsasaooooasdasduiuindvsdfsdfasdasdasd'

    sherlockAndAnagrams(s)






"""
    for i in range(0,len(s)):
            a = []
            b = []
            a.append(s[i])
            holder=1
    
            for k in range(i + 1, len(s)):
    
            for j in range(i + 1, len(s)):
                b.append(s[j])
    
                # Right Here is Where I Need to Check if they are anagrams.
                print(a, b)
                if a == b:
                    total += 1
    
                a.append(s[i + holder])
                holder += 1
    
    print(total)








"""

















