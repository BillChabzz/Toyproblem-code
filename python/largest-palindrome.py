# Solve the problem below using python
# Find largest palindrome
# A string is called palindrome when it is same while reading character by character from left side or right side.
# Given any arbitrary string find out the largest substring in it which is a palindrome.
# For example "anevitativehondacivic" returns "evitative"

#long solution
#def longestPalindrome(seq):
#    seqlEN = len(seq)
#    l = []
#    i= 0
#    palLen = 0
#    while i < seqLen:
#        if i > palLen and seq[i - palLen - 1] == seq[i]:
#            palLen += 2
#            i += 1
#            continue
#
#            l.append(palLen)
#
#            s = len(l) -2
#            e = s - palLen
#            for j in range(s,e, -1):
#                d = j - e - 1
#                if l[j] == d:
#                    palLen = d
#                    break
#                l.append(min(d, l[j]))
 #           else:
#                palLen = 1
#                i +=1
#    l.append(palLen)
#    lLen = len(l)
#    s = lLen -2
#    e = s - (2 * seqLen + 1 - lLen)
#    for i in range(s, e, -1):
#        d = i - e - 1
#        l.append(min(d, l[i]))
 #   return l


#shortsolution
def naiveLongestPalindromes(seq):

    seqLen = len(seq)
    lLen = 2 * seqLen + 1
    l = []

    for i in xrange(lLen):
        # If i is even (i.e., we're on a space), this will produce e
        # == s.  Otherwise, we're on an element and e == s + 1, as a
        # single letter is trivially a palindrome.
        s = i / 2
        e = s + i % 2

        # Loop invariant: seq[s:e] is a palindrome.
        while s > 0 and e < seqLen and seq[s - 1] == seq[e]:
            s -= 1
            e += 1

        l.append(e - s)

    return l
