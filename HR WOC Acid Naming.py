
# Acid Naming
# https://www.hackerrank.com/contests/w36/challenges/acid-naming

#!/bin/python3

import sys

def acidNaming(acid_name):
    end = acid_name[-2:]
    start = acid_name[:5]

    if 'hydro' in acid_name and end == 'ic':
        return ('non-metal acid')
    elif end == 'ic':
        return ('polyatomic acid')
    else:
        return ('not an acid')



x = 'hydrochloric'



result = acidNaming(x)
print(result)





















