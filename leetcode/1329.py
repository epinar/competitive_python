

def diagonalSort(mat):

    N, M = len(mat), len(mat[0])

    def sort(j, k):
        nums = []
        while j<N and k<M:
            nums.append(mat[j][k])
            j, k = j+1, k+1
        nums = sorted(nums)
        while j and k:
            j, k = j - 1, k - 1
            mat[j][k] = nums.pop()


    for i in range(M):
        sort(0, i)

    for i in range(1, N):
        sort(i, 0)
    return mat


mat = [[3,3,1,1],[2,2,1,2],[1,1,1,2]]
#mat = [[2],[1]]
print(diagonalSort(mat))