
# HR Sherlock and Anagrams Mk2
# https://www.hackerrank.com/challenges/sherlock-and-anagrams/problem?h_l=interview&playlist_slugs%5B%5D=interview-preparation-kit&playlist_slugs%5B%5D=dictionaries-hashmaps

"""
New idea,
Convert all letters to numbers,
a = 1
z = 26
Add all groups/pairs together, but also keep track of how many numbers/letters there are.


Example
abc = 36
a = 1, b = 2, c = 3
=6 and there are 3 of them so 36
Will require conversion between int and chr.
Each segment will have a different value, since there's no way to create the same number using the same amount of numbers.
# No this won't work


ad = 25
bc = 25





"""



a = 'abc'
b = 'cba'


print(hash(a))
print(hash(b))

















