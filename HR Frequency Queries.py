
# Frequency Queries
# https://www.hackerrank.com/challenges/frequency-queries/problem?h_l=interview&playlist_slugs%5B%5D%5B%5D=interview-preparation-kit&playlist_slugs%5B%5D%5B%5D=dictionaries-hashmaps

"""
Basically create an array and have various operations performed
c = command
1 means insert n into the array
2 means delete one occurence of n from the array
3 means check if there is an integer in the array with frequency of n

3 is the only thing I need to print out.
0 if there are no matches, 1 if there is at least one match.



Idea
Create a frequency dictionary.
And regular dict
So if I add 9 to the dict, freqD key =1 value = 9 and any others at that amount.
So if I add another 9, freqD at 2 =9 and remove 9 from freqD key = 1




Completed
Things I learned
For time efficiency do not swap between calculations and printing if possible.
Store answers for later and print all at once.
Be careful when adding/remove dictionary values if an entry doesn't exist for them.
Many errors appear this way
Learn to use discard instead of remove for times when I don't know if the value even exists.










"""

dictN = {}
freqD = {}
"""
1 == Add
2 == Remove
3 == Print


"""
q = int(input())
ans = []
for i in range(q):

    c,n = map(int, input().split(' '))

    #print(c,n)


    # ADD
    if c == 1:
        if n in dictN:
            dictN[n]+=1
        else:
            dictN[n]=1
        # Increase Frequency
        newFreq = dictN[n]
        prevFreq = newFreq-1
        if prevFreq in freqD:
            freqD[prevFreq].discard(n)

        if newFreq in freqD:
            freqD[newFreq].add(n)
        else:

            freqD[newFreq] = set()
            freqD[newFreq].add(n)
    # Remove
    elif c == 2:
        if n in dictN:
            dictN[n]-=1
            if dictN[n] == -1:
                dictN[n] = 0
        else:
            dictN[n]=0
        # Increase Frequency
        newFreq = dictN[n]
        prevFreq = newFreq+1
        # Likely problems here.
        # What if newFreq == -1??

        if prevFreq in freqD:
            freqD[prevFreq].discard(n)

        if newFreq in freqD:
            freqD[newFreq].add(n)
        else:

            freqD[newFreq] = set()
            freqD[newFreq].add(n)
    elif c == 3:
        if n in freqD:
            if(len(freqD[n])) > 0:
                ans.append(1)
            else:
                ans.append(0)
        else:
            ans.append(0)



for i in ans:
    print(i)







