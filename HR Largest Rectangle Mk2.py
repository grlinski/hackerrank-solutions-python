
# Largest Rectangle
# https://www.hackerrank.com/challenges/largest-rectangle/problem


# Apparently I Already Solved This
# Let's see if I can do it better
# Done!

# Adding Notes

# This is just a basic function to declutter things
# Calculates the height of the rectangles
def calc_height(h,w1,w2):

    height = h*abs(w1-w2)
    return height


# Inputs, r is the list of Buildings
n = int(input())
r = list(map(int, input().strip().split(' ')))
# One last one added since my calculations don't start until there is a building smaller than a preceeding one.
r.append(0)

# Buildings
# This is the list of buildings, more technically rectangles but whatever
# Each building is designated by first its height, then its index
# To be a bit more technical, the first number is the height, the second number is the index of where the first building of its height or less is located.
# No point in storing a building of the same height.
b = [[0,0]]

# Answer
largest = 0

# Walking through the list of buildings
for i in range(0,len(r)):
    # Position is i
    # Building is r[i]
    if b[-1][0] < r[i]:
        q = []
        q.append(r[i])
        q.append(i)

        b.append(q)
    elif b[-1][0] == r[i]:
        pass
    else:
        while r[i] < b[-1][0]:
            x = b.pop(-1)
            h = (calc_height(x[0],x[1],i))
            largest = max(largest,h)
        q = []
        q.append(r[i])
        q.append(x[1])
        b.append(q)

h = (calc_height(b[-1][0],b[-1][1],len(r)))
largest = max(largest,h)



print(largest)
#print(b)

"""
So what exactly does this all do.
Note, the b and r lists probably should have swapped variable names.
So as we go through each of the buildings, r list, we check its height compared to the last item in our b list. Which works like a stack more or less. I only want to access b list from it's topmost entry.
So anyways if the new building has a greater height than the previous, the new building is appended to my stack alongside its index number.
If they are equal, I ignore it.
If the new building is smaller than the previous then I pop the previous out of the stack. 
So I pop out a building, with its height and also an index number. This index number originally tells me where this building started. However later on it may indicate where a building of larger or same height started at.
For example if I have 11,12,10,8. The 8 building will eventually take the index of the 11 building. Since when going back we can still make a rectangle streching back with a height of 8.
Anyways I have the height, index number and the current index number.
The differences of the indexes indicate the width. So with this I can calculate a rectangle. I store the max rectangle.
This keeps going through the stack comparing the current building to the topmost entry of the stack until we end at a smaller building. Note that 0 was added to the list so we never actually empty the front of the stack.
When we hit a smaller building, we add the current building and give it the index number of the last building it removed. Since we know that this building can form a rectangle that extend to there.
And actually that's all of it. There is one more calculation once the list ends as there may not be a final computation unless the last item is smaller than the previous.







"""
















