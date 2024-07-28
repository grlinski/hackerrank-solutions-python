
# https://www.hackerrank.com/challenges/designer-pdf-viewer/problem
# Designer PDF Viewer
"""

INput
26 integers
word




"""


def designerPdfViewer(h, word):
    largest = 0

    wordsize = len(word)
    for i in word:
        print("Next")
        x = ord(i)
        x= x-97
        x = h[x]
        largest = max(largest,x)
    answer = largest*wordsize


    return answer




h = list(map(int, input().strip().split(' ')))
word = input().strip()


print(designerPdfViewer(h,word))





















