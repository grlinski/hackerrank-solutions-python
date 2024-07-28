

# https://www.hackerrank.com/challenges/ctci-ransom-note/problem?h_l=playlist&slugs%5B%5D=interview&slugs%5B%5D=interview-preparation-kit&slugs%5B%5D=dictionaries-hashmaps
# Ransom Note

def checkMagazine(magazine, note):
    for i in magazine:
        if i in note:
            note.remove(i)
        if len(note) == 0:
            return "Yes"

    return 'No'





m,n = map(int, input().split(' '))
mag = input().split()
note = input().split()

print(checkMagazine(mag, note))












