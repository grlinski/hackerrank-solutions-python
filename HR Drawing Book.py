
# Drawing Book
# https://www.hackerrank.com/challenges/drawing-book/problem




"""

n page book
open to page number n

Page 1 is the first right page
Turning a page goes through two pages

Going from either the front or back one page at a time
What is the minimum amount of page turns needed

Start from either page 0,1
Or the back at n

input
n pages
p wanted page


"""

# !/bin/python3

import sys


def solve(n, p):
    mid = n / 2
    diff = n - p
    diffpages = int(diff / 2)

    # From the Back or Front
    # Front
    if p <= mid:
        x = int(p / 2)
        return (x)
    else:
        if n % 2 == 0:
            if n - p == 1:
                return 1

        return (diffpages)


n = int(input().strip())
p = int(input().strip())
result = solve(n, p)
print(result)



















