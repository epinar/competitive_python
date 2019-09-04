
import unittest

def lengthOfLongestSubstring(s: str) -> int:

    res = 0
    sub = ''
    for ch in s:
        f = sub.find(ch)
        sub += ch
        if f == -1:
            res = max(len(sub), res)
        else:
            sub = sub[f+1:]
    return res

def lengthOfLongestSubstring2(s: str) -> int:

    used = {}
    res = 0
    sub = ''
    for i, ch in enumerate(s):
        sub += ch
        if ch in used and (i - len(sub)) <= used[ch]:
            ind = used[ch] - (i - len(sub))
            sub = sub[ind:]
        else:
            res = max(len(sub), res)
        used[ch] = i
    return res

def lengthOfLongestSubstring3(s: str) -> int:

    used = {}
    res = 0
    st = 0
    for i, ch in enumerate(s):
        if ch in used and st <= used[ch]:
            st = used[ch]+1
        else:
            res = max(i-st+1, res)
        used[ch] = i
    return res

class Testing(unittest.TestCase):

    def test_length(self):
        cases = [
            ['abcabcbb', 3],
            ["bbbbb", 1],
            ["pwwkew", 3],
            ['  ', 1],
            ['b', 1],
            ['', 0],
            ["aab", 2]
        ]

        f1 = lengthOfLongestSubstring
        for i, x in enumerate(cases):
            self.assertEqual(f1(x[0]), x[1])
        f2 = lengthOfLongestSubstring2
        for i, x in enumerate(cases):
            self.assertEqual(f2(x[0]), x[1])
        f3 = lengthOfLongestSubstring3
        for i, x in enumerate(cases):
            self.assertEqual(f3(x[0]), x[1])

if __name__ == '__main__':
    unittest.main()
    print(lengthOfLongestSubstring2("aab"))