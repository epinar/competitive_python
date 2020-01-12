
def longestIncreasingPath_0(matrix):

    '''
    Straightforward recursive solution without memoization.
    '''

    if not matrix or not matrix[0]:
        return 0

    ans = 0

    def _findPath(vis, i, j):
        ans_loc = 0
        for a,b in [[i-1,j], [i+1, j], [i, j-1], [i, j+1]]:
            if len(matrix) > a >= 0 and len(matrix[0]) > b >= 0:
                if vis[a][b] == 0 and matrix[a][b] > matrix[i][j]:
                    vis[a][b] = 1
                    res_loc = _findPath(vis, a, b) + 1
                    ans_loc = max(ans_loc, res_loc)
                    vis[a][b] = 0
        return ans_loc

    zeros = [[0] * len(matrix[0]) for _ in range(len(matrix))]
    for i in range(len(matrix)):
        for j in range(len(matrix[0])):
            zeros[i][j] = 1
            res = _findPath(zeros, i, j) + 1
            ans = max(ans, res)
            zeros[i][j] = 0
    return ans

def longestIncreasingPath_1(matrix):

    '''
    Extend the previous solution with memoization.
    '''

    if not matrix or not matrix[0]:
        return 0

    def dfs(i, j):
        if not dp[i][j]:
            ans_loc = 0
            for a, b in [[i - 1, j], [i + 1, j], [i, j - 1], [i, j + 1]]:
                if len(matrix) > a >= 0 and len(matrix[0]) > b >= 0:
                    if matrix[a][b] > matrix[i][j]:
                        res_loc = dfs(a, b)
                        ans_loc = max(ans_loc, res_loc)
            dp[i][j] = ans_loc+1
        return dp[i][j]


    M, N = len(matrix), len(matrix[0])
    dp = [[0] * N for _ in range(M)]
    ans = 0
    for i in range(M):
        for j in range(N):
            ans = max(dfs(i, j), ans)
    return ans



nums1 = [
    [9, 9, 4],
    [6, 6, 8],
    [2, 1, 1]
]

nums2 = [
  [3,4,5],
  [3,2,6],
  [2,2,1]
]

nums3 = [
    [3, 2, 1],
    [4, 5, 6]
]

nums4 = [[1]]

nums5 = [[0],[1],[5],[5]]

nums6 = [
    [4,3,2,1],
    [3,5,1,1]
]

ans = longestIncreasingPath_1(nums6)
print(ans)