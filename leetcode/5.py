
import unittest

def longestPalindrome(s: str) -> str:

    res = ''
    res_len = 0
    for i, x in enumerate(s):

        ## Check odd length palindrome
        l, r = i, i
        while l>=0 and r<len(s) and s[l] == s[r]:
            l-=1
            r+=1

        curr = s[l+1:r]
        if len(curr) > res_len:
            res = curr
            res_len = len(curr)

        ## Check even length palindrome
        l, r = i-1, i
        while l>=0 and r<len(s) and s[l] == s[r]:
            l-=1
            r+=1

        curr = s[l+1:r]
        if len(curr) > res_len:
            res = curr
            res_len = len(curr)

    return res

def longestPalindrome_manacher(s):

    '''
    Calculate the largest possible palindrome at a current indice.
    If it is the longest seen palindrome, update it.
    For the next indices, if they are within the range of the longest palindrome,
    since they were already calculated, use that knowledge.
    If it is still possible to expand that substring, expand and check
    if it is larger than the longest palindrome.
    '''

    # Transform S into T.
    # For example, S = "abba", T = "^#a#b#b#a#$".
    # ^ and $ signs are sentinels appended to each end to avoid bounds checking
    T = '#'.join('^{}$'.format(s))
    n = len(T)
    P = [0] * n
    C = R = 0 # C is the center of the longest palindrome, r is the leftmost indice of that.
    print(T)
    for i in range(1, n - 1):
        # Case 1, a palindrome's left part is mirrored to the right part.
        P[i] = (R > i) and min(R - i, P[2 * C - i])  # equals to i' = C - (i-C)

        # Use the current knowledge of the subpalindrome, then see if it is possible
        # to expand it centered at i.
        while T[i + 1 + P[i]] == T[i - 1 - P[i]]:
            P[i] += 1
            print(i, "hey")

        # If palindrome centered at i expand more than R (bigger than max palindrome)
        # update the center based on expanded palindrome.
        if i + P[i] > R:
            C, R = i, i + P[i]

        print(i, C, R, P)
    # Find the maximum element in P.
    maxLen, centerIndex = max((n, i) for i, n in enumerate(P))
    return s[(centerIndex - maxLen) // 2: (centerIndex + maxLen) // 2]

class Testing(unittest.TestCase):

    def test_palindrome(self):

        cases = [
            ["babad", "bab"]
        ]

        f1 = longestPalindrome
        for i, x in enumerate(cases):
            self.assertEqual(f1(x[0]), x[1])

if __name__ == '__main__':
    print(longestPalindrome_manacher("dacabacad"))