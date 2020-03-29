


def matrixScore_draft(A):

    if len(A)==0:
        return 0

    N, M = len(A), len(A[0])

    print(A)

    # search toggles here

    # count sum
    num = 0
    for i, lis in enumerate(A):
        s = ""
        for val in lis:
            s = s+str(val)
        num += int(s, 2)

    return num


def matrixScore_long(A):
    R, C = len(A), len(A[0])

    colsums = [0] * C
    for r in range(R):
        for c in range(C):
            colsums[c] += A[r][c]

    ans = 0
    for r in range(1 << R):
        if r:
            trans = r ^ (r - 1)
            for bit in range(R):
                if (trans >> bit) & 1:
                    for c in range(C):
                        colsums[c] += -1 if A[bit][c] else +1
                        A[bit][c] ^= 1

        score = sum(max(x, R - x) * (1 << (C - 1 - c))
                    for c, x in enumerate(colsums))
        ans = max(ans, score)

    return ans

def matrixScore(A):
    R, C = len(A), len(A[0])
    ans = 0
    for c in range(C):
        col = 0
        for r in range(R):
            col += A[r][c] ^ A[r][0]
        ans += max(col, R - col) * 2 ** (C - 1 - c)
    return ans


mat = [[0,0,1,1],[1,0,1,0],[1,1,0,0]]
print(matrixScore(mat))