import heapq

def isConnected(grid, T):

    N = len(grid)

    if grid[0][0]>T:
        return False

    def dfs(vis, i, j):

        if i == j == N-1:
            return True

        for a, b in [[i - 1, j], [i + 1, j], [i, j - 1], [i, j + 1]]:
            if 0 <= a < N and 0 <= b < N:
                if grid[a][b] <= T and vis[a][b] == False:
                    vis[a][b] = True
                    if dfs(vis, a, b):
                        return True
                    else:
                        vis[a][b] = False
        return False

    visited = [[0]*N for i in range(N)]
    return dfs(visited, 0, 0)

def bfs(grid, T):

    N = len(grid)
    if grid[0][0]>T:
        return False
    bfs = [(0,0)]
    vis = [[0] * N for i in range(N)]
    while len(bfs):
        i, j = bfs.pop(0)
        if grid[i][j] <= T:
            if i == j == N-1:
                return True
            for a, b in [[i - 1, j], [i + 1, j], [i, j - 1], [i, j + 1]]:
                if 0 <= a < N and 0 <= b < N and vis[a][b] == False:
                        vis[a][b] = True
                        bfs.append((a, b))
    return False

def swimInWater(grid):
    N = len(grid)
    l, r = 0, N*N - 1

    while l < r:
        mid = (l+r)//2
        print(mid, l, r, grid)
        if bfs(grid, mid):
            r = mid
            print("yes")
        else:
            l = mid+1

    return r

def swimInWater2(grid):
    N, pq, seen, res = len(grid), [(grid[0][0], 0, 0)], set([(0, 0)]), 0
    while True:
        T, x, y = heapq.heappop(pq)
        res = max(res, T)
        print(res, T, x, y)
        if x == y == N - 1:
            return res
        for i, j in [(x + 1, y), (x, y + 1), (x - 1, y), (x, y - 1)]:
            if 0 <= i < N and 0 <= j < N and (i, j) not in seen:
                seen.add((i, j))
                heapq.heappush(pq, (grid[i][j], i, j))

g1 = [[0, 2], [1, 3]]

g2 = [[0, 1, 2, 3, 4], [24, 23, 22, 21, 5], [12, 13, 14, 15, 16], [11, 17, 18, 19, 20], [10, 9, 8, 7, 6]]

g3 = [[3,2],[0,1]]

print(swimInWater2(g1))
print(bfs(g2, 16))


grid = [[0, 1, 1],
        [0, 0, 1],
        [0, 0, 0]]

#print(isConnected(grid,1))
