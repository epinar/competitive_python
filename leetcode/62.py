

def uniquePaths(m, n):

    if m == 0 or n == 0:
        return 0

    if m ==1 or n ==1:
        return 1

    dp = [[0]*n for i in range(m)]

    for i in range(1, n):
        dp[0][i] = 1

    for i in range(1, m):
        dp[i][0] = 1

    for i in range(1, m):
        for j in range(1, n):
            dp[i][j] = dp[i][j-1] + dp[i-1][j]

    return dp[m-1][n-1]

def uniquePaths2(m, n):
    ### Math solution, (m+n)! / (m! * n!)

    if m == 1 or n == 1:
        return 1

    m, n = m-1, n-1

    if n > m: # keep m bigger
        m, n = n, m

    res = 1
    for i in range(1, n+1):
        res *= (m+i)
        res /= i

    return int(res)

print(uniquePaths(7, 3))
print(uniquePaths2(7, 3))