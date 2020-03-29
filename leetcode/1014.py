

def maxScoreSightseeingPair(A):

    l, r = 0, 1
    N = len(A)
    res = A[l] + A[r] + l - r
    for i in range(2, N):
        if A[i] + A[r] + r - i >= res and A[i] + A[r] + r - i > A[i] + A[l] + l - i:
            l, r = r, i
            res = A[l] + A[r] + l - r
        elif A[i] + A[l] + l - i > res:
            r = i
            res = A[l] + A[r] + l - r

        if A[i] + A[i - (r-l)] + l - r >= res:
            l, r = i - (r-l), i
            res = A[l] + A[r] + l - r

    print(l, r)
    return res

A = [1,8,1,5,2,1,6] # 11
#A = [4,7,5,8] # 13
#A = [7,2,6,6,9,4,3] # 14
A = [6,3,7,4,7,6,6,4,9]
print(maxScoreSightseeingPair(A))