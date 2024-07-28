

# A Race Against Time Mk1
# https://www.hackerrank.com/contests/w36/challenges/a-race-against-time


import sys



# Swaps Current With the New Value, adds Time to TTotal and Price to Ptotal
# Also Accounts for time position movement
def swap(current,new,ttotal,ptotal,price):
    diff = abs(new-current)
    ttotal = ttotal+diff
    ptotal = ptotal+price

    return new,ttotal,ptotal


def noswap(current,ttotal):
    ttotal = ttotal
    return current,ttotal


def equal(ttotal,ptotal,price):
    ttotal = ttotal
    ptotal = ptotal+price
    return ttotal,ptotal


def next_x_cases(times,current,start,h,ttotal,ptotal,p,n):
    # We Already Start on the current start so add one
    start+=1
    if start >= n or start+times >=n:
        return current,ttotal,ptotal
    else:
        for i in range(start,start+times):
            if h[i] > current:
                current, ttotal, ptotal = swap(current, h[i], ttotal, ptotal, p[i])
            elif h[i] == current and p[i] <0:
                ttotal,ptotal = equal(ttotal,ptotal,p[i])

        return current,ttotal,ptotal



def raceAgainstTime(n, mason, h, p):
    ptotal = 0
    ttotal = 0
    hmini = 0
    hmaxi = 0
    pmini = 0
    pmaxi = 0
    current = mason
    for i in range(0,n-1):
        #print('Position: ',i)
        #print('Time ', ttotal)
        #print('Price ', ptotal)
        #print('Current Height', current)

        # Must hand off if new height greater
        if h[i] > current:
            # Swap function
            current,ttotal,ptotal =  swap(current,h[i],ttotal,ptotal,p[i])
            #print('High Swap')

        # If the height is the same and the price is negative switch
        elif h[i] == current and p[i] <0:
            # Equal Function
            ttotal,ptotal = equal(ttotal,ptotal,p[i])
            #print('Equal')


        # Optional Switches
        elif h[i] < current:
            # Exploratory Variables
            # Does 5 Cases of each, one swap and no swap
            # Takes whichever works out better, ie) lower ttotal+ptotal, if both are equal take the one with lower height
            # Two Cases Either We Switch or We Don't
            # Swap and Didn't Swap
            # Once we hit another Swap Option, take the lower and that becomes the current

            swapc = h[i]
            swapttotal = 0
            swapptotal = 0

            noswapc = current
            noswapttotal = 0
            noswapptotal = 0

            # how many cases to try, 5 to start
            cases = 100
            if n-i < cases:
                cases = n-i
            else:
                swapc, swapttotal, swappctotal = next_x_cases(cases,swapc,i,h,ttotal,ptotal,p,n)
                noswapc, noswapttotal, noswappctotal = next_x_cases(noswapc, swapc, i, h, ttotal, ptotal, p,n)
                # Choose Lower
                if (swapttotal+swappctotal) <= (noswapttotal+noswapptotal):
                    current, ttotal, ptotal = swap(current, h[i], ttotal, ptotal, p[i])
                    #print('Low Swap')
                elif (swapttotal+swappctotal) > (noswapttotal+noswapptotal):
                    current, ttotal = noswap(current,ttotal)
                    #print('High Swap')

    ttotal = ttotal+n
    #print(ttotal,ptotal,current)
    return(ttotal+ptotal)








n = 14
mason_height = 5
heights = [2,3,1,5,4,7,8,3,6,2,3,6,4,1]
prices = [2,3,2,6,4,2,1,3,5,6,4,2,3,3]
#result = raceAgainstTime(n, mason_height, heights, prices)




n = 4
mh = 5
h = [2, 6, 2]
p = [2, 3, 2]
print(raceAgainstTime(n, mh, h, p))



"""
n = 4
mh = 5
h = [2, 3, 1]
p = [2, 3, 2]
print(raceAgainstTime(n, mh, h, p))
"""









"""
What the Question is Asking

Two Students
Madison and Mason
Mason starts with the Baton
Mdison recieves the baton at the end
Students inbetween MM and the students heights are given
Mason's height is given too


The baton holder can hand over the baton to the student at the current position 
Or move to the next position
If the student at the given position is taller than the current carrier they must hand it over

Takes one second to move between consecutive positions
When the baton is handed over there is a time and price associated with it

The time taken in seconds is the abs difference betwen the heights of the current carried and the student to whom it is handed
time = abs(height1-height2)

The student to whom the baton is passed charges a price
The price can be negative

Find the minimum money and time 


Input
Number of People, exluding Mason and Madison
Mason's Height
List of Students Heights
List of Prices They Charge



"""



"""
Sample Case
10
5
6 1 2 7 3 6 1 2 7
-2 -7 7 -2 -13 -2 -7 7 -2




"""
"""

Create Algorithm of Most Common Height Values
Or Create an index of heights compared to their prices, lower better, negative best


********
Alg that checks an optional swap
Goes until there is another optional swap.
If the swap is better the swap goes ahead
Otherwise it doesn't










"""





