
from heapq import heappush, heappop

def getSkyline(buildings):

    ans = [[0,0]]

    q = []
    for b in buildings:
        q.append([b[0], -b[2], b[1]])
        q.append([b[1], 0, 0])
    q.sort()

    #print(q)
    s = [(0, float('inf'))]
    for i in range(len(q)):
        l = q[i][0]
        h = q[i][1]
        r = q[i][2]

        # Remove the events before current event.
        while s[0][1] <= l:
            heappop(s)

        if h != 0:
            heappush(s, (h, r))

        if ans[-1][1] != -s[0][0]:
            ans.append([l, -s[0][0]])

        #print(i, " ", s)

    return ans[1:]

b = [[2, 9, 10], [3, 7,15], [5, 12, 12], [15, 20, 10], [19, 24, 8]]
print(getSkyline(b))
print(getSkyline([[0,2,3],[2,5,3]]))
print(getSkyline([[1,2,1],[1,2,2],[1,2,3]]))