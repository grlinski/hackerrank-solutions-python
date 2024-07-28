
# Super Reduced String
# https://www.hackerrank.com/challenges/reduced-string/problem




def super_reduced_string(x):
    x = x+"x"
    counter = 1
    ns=""

    while counter!=0:
        counter=0
        hold = 0


        while hold < len(x)-1:
            if x[hold] != x[hold+1]:
                ns = ns+x[hold]
                print(ns)
            else:
                counter+=1
                hold = hold+1
            hold+=1


        x = ns
        ns=""

    if x == "":
        x = "Empty String"

    return x







q = "aaabccddd"

print(reduced(q))


















