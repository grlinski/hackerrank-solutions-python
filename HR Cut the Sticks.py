#Cut the Sticks
# Each stick is cut by the smallest stick of the group
# Then the process is repeated again
# Each time print out the amount of sticks left.
# Obviously if a stick is reduced to zero or below it is gone


#Setup values, n and arr are used in the actual problem
n = int(input())
arr = [5, 4, 4, 2, 2, 8]




# The Main Loop
# Continues to go until there are no values left in arr, when its length = 0
while n > 0:
    print(n)
    arr2 = []
    #Cutval is just set to a high value so all the sticks in the array will be less than it
    cutval = 1000



    #Finding the smallest stick
    for i in range(0,n):
        if cutval > arr[i]:
            cutval = arr[i]

    #Cutting
    for i in range(0,n):
        arr[i] = arr[i]-cutval
        if arr[i] > 0:
            arr2.append(arr[i])

    #Transfering arr2 into arr
    arr = arr2
    # Finding out the amount of values within the array
    n = len(arr)






































