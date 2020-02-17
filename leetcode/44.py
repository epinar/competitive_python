

def isMatch2(str, pattern):


    s = 0
    p = 0
    match = 0
    star = -1


    while s < len(str):
        if p < len(pattern) and (pattern[p] == "?" or pattern[p]==str[s]):
            s += 1
            p += 1
        elif p < len(pattern) and pattern[p] == "*":
            star = p
            match = s
            p += 1
        elif star != -1:
            p = star + 1
            match += 1
            s = match
        else:
            return False

    while p < len(pattern) and pattern[p] == "*":
        p += 1


    return len(pattern) == p

def isMatch(s, p):

    if len(p) == 0 and len(s) != 0:
        return False

    if len(s) == 0 and len(p.replace("*", ""))== 0:
        return True

    M , N = len(p), len(s)
    dp = [[False]*N for i in range(M)]

    if s[0] == p[0] or p[0]== "*" or p[0]== "?":
        dp[0][0] = True

    for j in range(1, N):
        if dp[0][j-1] and p[0]=="*":
            dp[0][j] = True

    #print(dp)

    for i in range(1, M):
        if dp[i-1][0] and (p[i]=="*" or p[i]=="?" or s[0]==p[i]):
            dp[i][0] = True

    #print(dp)

    for i in range(1, M):
        for j in range(1, N):
            if (dp[i-1][j-1] and (s[j]==p[i] or p[i]=="?")) or p[i]=="*":
                dp[i][j] = True

    #print(dp)

    return dp[M-1][N-1]


s = "aa"
p = "a"
print(isMatch2(s, p))


s = "aa"
p = "*"
print(isMatch2(s, p))

s = "cb"
p = "?a"
print(isMatch2(s, p))

s = "adceb"
p = "*a*b"
print(isMatch2(s, p))


s = "acdcb"
p = "a*c?b"

#print(isMatch2(s, p))



s = "abcde"
p = "??"

#print(isMatch2(s, p))

s = ""
p = "*"

#print(isMatch(s, p))