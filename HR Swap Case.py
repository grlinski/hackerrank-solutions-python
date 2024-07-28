

# Swap Case
# https://www.hackerrank.com/challenges/swap-case/problem




def swap_case(s):
    ns = ""
    for i in s:
        x = ord(i)
        # Upper to Lower
        if x >= 65 and x <= 90:
            x = x+32
        elif x >=90 and x <=122:
            x = x-32
        ns = ns+chr(x)
    return ns




print(swap_case("AAZZ aazz"))










