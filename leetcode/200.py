
def numIslands(grid):
    N, M = len(grid), len(grid[0])
    ans = 0

    def traverse(a, b):
        if 0<=a<N and 0<=b<M and grid[a][b] == 1:
            grid[a][b] = 0
            traverse(a - 1, b)
            traverse(a + 1, b)
            traverse(a, b - 1)
            traverse(a, b + 1)
        return

    for i in range(N):
        for j in range(M):
            if grid[i][j] == 1:
                traverse(i, j)
                ans += 1
    return ans



if __name__ == '__main__':
    grid = [[1, 1, 1, 1, 0],
        [1, 1, 0, 1, 0],
        [1, 1, 0, 0, 0],
        [0, 0, 0, 0, 0]
    ]
    grid = [[1, 1, 0, 0, 1],
            [1, 1, 0, 1, 0],
            [0, 0, 1, 0, 0],
            [0, 0, 0, 1, 1]
            ]

    print(numIslands(grid))