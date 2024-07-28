
# Sorting Comparator
# https://www.hackerrank.com/challenges/ctci-comparator-sorting/problem?h_l=interview&playlist_slugs%5B%5D%5B%5D=interview-preparation-kit&playlist_slugs%5B%5D%5B%5D=sorting


n = int(input())

list1 = []
for i in range(n):
    s = input().split()
    name = s[0]
    score = int(s[1])
    list1.append([score,name])

#list1.sort(reverse=True)
list1 = sorted(list1, key = lambda x: (1000-x[0],x[1]))

for i in list1:
    print(i[1],i[0])


