
# HR Making Anagrams
# https://www.hackerrank.com/challenges/ctci-making-anagrams/problem?h_l=interview&playlist_slugs%5B%5D=interview-preparation-kit&playlist_slugs%5B%5D=strings



a = input()
b = input()

lista = [0]*26
listb = [0]*26




for i in range(0,max(len(a),len(b))):
    #print(ord(a[i]))
    try:
        lista[ord(a[i])-97]+=1
    except:
        pass

    try:
        listb[ord(b[i])-97]+=1
    except:
        pass


total = 0
for i in range(0,26):
    total+= abs(lista[i]-listb[i])

print(total)


















