

def isMatch(s: str, p: str) -> bool:

    if len(p) == 0:
        return len(s) == 0

    first = False
    if len(s) > 0 and p[0] == s[0] or p[0] == '.':
        first = True

    if len(p) >= 2 and p[1] == "*":
        return (first and isMatch(s[1:], p) ) or isMatch(s, p[2:])
    else:
        return first and isMatch(s[1:], p[1:])

def isMatch2(s, p):

    memo = {}

    def dp(i, j):
        if (i, j) not in memo:
            if len(p) == j:
                res = len(s) == i
            else:
                first= len(s) > i and (p[j] == s[i] or p[j] == '.')
                if len(p) > j+1 and p[j+1] == "*":
                    res = (first and dp(i+1, j)) or dp(i, j+2)
                else:
                    res = first and dp(i+1, j+1)
            memo[i, j] = res
        return memo[i, j]
    return dp(0, 0)

def isMatch3(text, pattern):
    memo = {}

    def dp(i, j):
        if (i, j) not in memo:
            if j == len(pattern):
                ans = i == len(text)
            else:
                first_match = i < len(text) and pattern[j] in {text[i], '.'}
                if j + 1 < len(pattern) and pattern[j + 1] == '*':
                    ans = dp(i, j + 2) or first_match and dp(i + 1, j)
                else:
                    ans = first_match and dp(i + 1, j + 1)

            memo[i, j] = ans
        return memo[i, j]

    return dp(0, 0)

if __name__ == '__main__':
    s = 'ab'
    p = '.*'
    print(isMatch2(s, p))
    #print(bool(s))
    #print(p[0] in s[0])
    #print(p[0] in {s[0], '.'})