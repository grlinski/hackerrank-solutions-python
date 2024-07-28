

import math

# Viral Advertising
# https://www.hackerrank.com/challenges/strange-advertising/problem



def viralAdvertising(n):
    init = 5
    count = 0
    for i in range(0,n):

        init = math.floor(init/2)
        count = count+init
        init = init*3


    return count




print(viralAdvertising(4))


# 4 = 15















