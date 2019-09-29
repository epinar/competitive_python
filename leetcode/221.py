

def maximalSquare(matrix):

    N, M = len(matrix), len(matrix[0])

    ans = 0
    not_square = True
    for i in range(N):
        for j in range(M):
            #print("i, j : ", i , j)
            if matrix[i][j] == '1':
                not_square = False
                size_range = min(M-j, N-i)+1
                for size in range(size_range):
                    #print("size: ", size)
                    for k in range(size):
                        if not_square:
                            break
                        for l in range(size):
                            #print(" check: ", k, l)
                            if matrix[i+k][j+l] == '0':
                                not_square=True
                                #print("zero seen ")
                                break

                    if not_square:
                        break
                    else:
                        #print("new ans ", size)
                        ans = max(size, ans)
    return ans


def maximalSquare2(matrix):
    if len(matrix) == 0:
        return 0

    N, M = len(matrix), len(matrix[0])

    ans = 0
    dp = [[0]*M for _ in range(N)]
    for i in range(N):
        for j in range(M):
            if matrix[i][j] == '1':
                if i>0 and j >0 :
                    dp[i][j] = min(dp[i-1][j], dp[i-1][j-1], dp[i][j-1])+1
                else:
                    dp[i][j] = 1
                ans = max(dp[i][j], ans)

    return ans*ans


def maximalSquare3(matrix):
    '''
    DP solution with the same idea of 2, yet less memory. Instead of a 2D matrix,
    we can use an array, and keep the previous needed values (value above, and
    left corner) in variables.
    '''
    if len(matrix) == 0:
        return 0

    N, M = len(matrix), len(matrix[0])

    ans = 0
    dp = [0]*M
    prev = 0
    for i in range(N):
        for j in range(M):
            above = dp[j]
            if matrix[i][j] == '1':
                if j > 0:
                    dp[j] = min(dp[j-1], above_left, above)+1
                else:
                    dp[j] = 1
            else:
                dp[j] = 0
            above_left = above
            ans = max(dp[j], ans)
        #print(dp)
    return ans*ans


if __name__ == '__main__':
    matrix = [
        ["1","0","1","1","1"],
        ["1","0","1","1","1"],
        ["1","1","1","1","1"],
        ["1","0","0","1","0"]]

    matrix = [["1","0","1","1","1"],
              ["0","1","0","1","0"],
              ["1","1","0","1","1"],
              ["1","1","0","1","1"],
              ["0","1","1","1","1"]]

    print(maximalSquare3(matrix))