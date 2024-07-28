


# Gemstone
# https://www.hackerrank.com/challenges/gem-stones/problem



def gemstones(arr):
    gems = set()
    x = arr[0]
    newgems =set()

    # Get gems from first entry
    for i in range(0,len(x)):
        gems.add(x[i])

    for j in range(1,len(arr)):
        newgems = set()
        q = arr[j]
        for k in range(0,len(q)):
            x = q[k]
            if x in gems:
                newgems.add(x)
        gems = newgems
    return gems


# set.remove('a')



q = ['abcccededasfax', 'ababababab', 'eeeeea']

print(gemstones(q))


















