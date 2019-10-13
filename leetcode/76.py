from collections import *

def minWindow(s, t):

    '''
    Keep two pointers, left and right. Right moves to find the next possible
    set that has t. Then, left squeezes from left while checking if the string
    between them is still valid.
    We return the smallest fitting string seen.
    '''

    if not s or not t:
        return ""

    req = Counter(t)
    unique = len(req)
    window = {ch: 0 for ch in s}
    print(window)
    l = 0
    formed = 0 # Keeps a count of the required unique elements
    res = float("inf"), None, None
    for r, ch in enumerate(s):
        window[ch] = window[ch]+1

        if ch in req and window[ch] == req[ch]:
            formed += 1

        while l<=r and formed == unique:
            ch_left = s[l]

            if r - l + 1 < res[0]:
                res = (r-l+1, l, r)

            window[ch_left] -= 1
            if ch_left in req and window[ch_left]<req[ch_left]:
                formed -=1

            l += 1


    return "" if res[0] == float("inf") else s[res[1] : res[2]+1]



if __name__ == '__main__':
    S = "ADOBECODEBANC"
    T = "ABC"
    print(minWindow(S, T))