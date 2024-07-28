



def heightAndTotalHeight(arr):
    tree = []
    left = []
    right = []
    node1 = arr[0]
    level = 0
    tree.append([node1])
    for i in range(1,len(arr)):
        cur = arr[i]

        if cur < node1:
            level+=1
            tree[level].append(cur)













arr = [500, 400, 300, 450, 425, 475, 600, 550]
