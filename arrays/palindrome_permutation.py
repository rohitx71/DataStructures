"""
# https://www.hackerearth.com/problem/algorithm/palindrome-check-2-1/
# Very-Easy
Now, given a String S consisting of lowercase English alphabets, you need to find out whether any permutation of this
given String is a Palindrome. If yes, print "YES" (Without quotes) else, print "NO" without quotes.

SAMPLE INPUT
abab
SAMPLE OUTPUT
YES
"""


def check_permutation(s):
    h = set()
    for i in s:
        if i in h:
            h.remove(i)
        else:
            h.add(i)
    return len(h) <= 1


st = input()
if check_permutation(st):
    print("YES")
else:
    print("NO")



