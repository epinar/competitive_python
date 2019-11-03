

def minDistance(word1, word2):
    '''
    This algo is known as "levenshtein" distance, used in spelling correction or
    bioinformatics. We build up a matrix which represents the number of corrections
    between each character of the word. Last element of this matrix gives the result.
    '''

    n, m = len(word1), len(word2)
    dp = [[0 for i in range(m + 1)] for j in range(n + 1)]

    for i in range(n+1):
        for j in range(m+1):
            if i == 0:
                dp[i][j] = j
            elif j == 0:
                dp[i][j] = i
            elif word1[i-1] == word2[j-1]:
                dp[i][j] = dp[i-1][j-1]
            else:
                dp[i][j] = min(dp[i][j-1], dp[i-1][j], dp[i-1][j-1])+1

    return dp[n][m]

def minDistance2(word1, word2):
    '''
    Same logic with previous one but the space is reduced from O(mn) to O(n) now.
    Instead of keeping all rows of the matrix, it keeps only the last one because only
    that is needed.
    '''
    n, m = len(word1), len(word2)
    dp = [0] * (m+1)
    for i in range(n+1):
        for j in range(m+1):
            if i == 0 and  j == 0: continue
            elif i == 0:
                dp[j] = dp[j-1]
            elif j == 0:
                dp[j] = dp[j] + 1
            elif word1[i-1] == word2[j-1]:
                dp[j] = pre[j-1]
            else:
                dp[j] = min(pre[j-1], dp[j], dp[j-1])+1
        pre = dp[:]

    return dp[-1]



if __name__ == '__main__':
    print(minDistance2("", ""))
    print(minDistance2("horse", "ros"))
    print(minDistance2("intention", "execution"))