
def maxIncreaseKeepingSkyline(grid):

    N, M = len(grid), len(grid[0])
    max_row, max_col = [0]*N, [0]*M

    for i in range(N):
        max_row[i] = max(grid[i])
        for j in range(M):
            max_col[j] = max(max_col[j], grid[i][j])

    sum = 0
    for i in range(N):
        for j in range(M):
            new_height = min(max_row[i], max_col[j])
            diff = new_height - grid[i][j]
            sum += diff

    return sum


def maxIncreaseKeepingSkyline2(grid):
    rows, cols = list(map(max, grid)), list(map(max, zip(*grid)))
    return sum(min(i, j) for i in rows for j in cols) - sum(map(sum, grid))


if __name__ == '__main__':
    grid = [[3, 0, 8, 4], [2, 4, 5, 7], [9, 2, 6, 3], [0, 3, 1, 0]]
    #grid = [[1]]
    print(maxIncreaseKeepingSkyline2(grid))
