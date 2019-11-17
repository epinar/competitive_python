
import collections


def dominatedSub(arr):

    if len(arr)<2:
        return -1

    d = collections.defaultdict()
    minlen = float('inf')
    for i, v in enumerate(arr):
        if v not in d:
            d[v] = i
        else:
            l = i - d[v] + 1
            if l < minlen:
                minlen = l
            d[v] = i

    if minlen == float('inf'):
        minlen=-1

    return minlen


if __name__ == '__main__':

    q = int(input())
    for i in range(q):
        n = map(int, input().split())
        arr = list(map(int, input().split()))
        res = dominatedSub(arr)
        print(res)