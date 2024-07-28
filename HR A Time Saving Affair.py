
# A Time Saving Affair
# https://www.hackerrank.com/contests/w38/challenges/a-time-saving-affair

"""

n juunctions numbered 1 to n
m bidirectional roads connecting some pairs of junctions
Each road takes some amount of time to pass through
At every junctions there are traffic lights, red = stop, green = go

Traffic signal changes colour every k seconds
Initally a time 0 traffic lights are green at all junctions


Input
n number of junctions
k time it takes a signal to change its colour
m roads
The next m lines
i j t
i and j denotes a road between two junctions
t denotes time required to travel through it




"""



def createJunction(source,dest,time,mapper):

    try:
        mapper[source] = (dest,time)
    except:
        pass






def leastTimeToInterview(n, k, m):
    # Return the least amount of time needed to reach the interview location in seconds.















