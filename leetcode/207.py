

def canFinish(numCourses, prerequisites):
    # dfs

    g =[[] for _ in range(numCourses)]
    visited = [0 for _ in range(numCourses)]

    for x, y in prerequisites:
        g[x].append(y)

    def dfs(i):
        if visited[i] == 1:
            return True
        if visited[i] == -1:
            return False
        visited[i] = -1
        for dep in g[i]:
            if not dfs(dep):
                return False
        visited[i] = 1
        return True

    for i in range(numCourses):
        if not dfs(i):
            return False
    return True

def canFinish2(numCourses, prerequisites):
    # Topological sort, bfs
    from collections import deque
    graph = [[] for _ in range(numCourses)]
    indeg = [0 for _ in range(numCourses)]
    for x,y in prerequisites:
        graph[x].append(y)
        indeg[y] += 1
    q = deque()
    for i in range(numCourses):
        if not indeg[i]:
            q.append(i)
    k = 0
    while q:
        n = q.popleft()
        for dep in graph[n]:
            indeg[dep] -= 1
            if indeg[dep] == 0:
                q.append(dep)
        k += 1
    return k == numCourses

def canFinish3(n, pres):
    # Same solution with 3
    from collections import deque
    ind = [[] for _ in range(n)]  # indegree
    oud = [0] * n  # outdegree
    for p in pres:
        oud[p[0]] += 1
        ind[p[1]].append(p[0])
    dq = deque()
    for i in range(n):
        if oud[i] == 0:
            dq.append(i)
    k = 0
    while dq:
        x = dq.popleft()
        k += 1
        for i in ind[x]:
            oud[i] -= 1
            if oud[i] == 0:
                dq.append(i)
    return k == n


if __name__ == '__main__':


    print(canFinish2(2, [[1, 0], [0,1]]))
    print(canFinish2(5, [[2,1],[4,2],[2,3], [1,4]]))
    print(canFinish2(5, [[2,1],[4,2],[2,3]]))
    print(canFinish2(3, [[1,0], [2,1]]))
    print(canFinish2(3, []))