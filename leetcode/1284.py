
from copy import deepcopy
from itertools import chain
from collections import deque

def minFlips(mat):

    ### Breadth first search. Save the state of the grid at each step along with the timestep.
    ### Apply the next flip. Search if it was not seen before (put it in stack).
    ### Return state if all are zero.

    m, n = len(mat), len(mat[0])

    astr = str(list(chain.from_iterable(mat)))
    stack = deque([(mat, 0)])
    visited = set()
    visited.add(astr)

    while stack:
        matrix, time = stack.popleft()
        if sum(sum(matrix,[])) == 0:
            return time

        for i in range(m):
            for j in range(n):
                temp = deepcopy(matrix)
                for x, y in [(i, j), (i-1, j), (i+1, j), (i, j-1), (i, j+1)]:
                    if m > x >=0 and n > y >= 0:
                        temp[x][y] ^= 1
                astr = str(list(chain.from_iterable(temp)))
                if astr not in visited:
                    stack.append((temp, time+1))
                    visited.add(astr)
    return -1


def minFlips2(mat):

    ### Depth first search. Save the state of the grid at each step along with the timestep.
    ### Apply the next flip. Search if it was not seen before (put it in stack).
    ### Return state if all are zero.

    m, n = len(mat), len(mat[0])

    astr = str(list(chain.from_iterable(mat)))
    stack = deque([(mat, 0)])
    visited = set()
    visited.add(astr)

    while stack:
        matrix, time = stack.popleft()
        if sum(sum(matrix,[])) == 0:
            return time

        for i in range(m):
            for j in range(n):
                temp = deepcopy(matrix)
                for x, y in [(i, j), (i-1, j), (i+1, j), (i, j-1), (i, j+1)]:
                    if m > x >=0 and n > y >= 0:
                        temp[x][y] ^= 1
                astr = str(list(chain.from_iterable(temp)))
                if astr not in visited:
                    stack.append((temp, time+1))
                    visited.add(astr)
    return -1

mat = [[0,0],[0,1]]
mat = [[1,1,1],[1,0,1],[0,0,0]]
mat = [[1,0,0],[1,0,0]]
print(minFlips(mat))