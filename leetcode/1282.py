

def groupThePeople(groupSizes):

    n = len(groupSizes)
    d = {}
    for i in range(1, n+1):
        d[i] = []

    for i, val in enumerate(groupSizes):
        d[val].append(i)

    res = []

    for k, v in d.items():
        if len(v) != 0:
            arrs = [v[x:x+k] for x in range(0, len(v), k)]
            res += arrs

    return res

import collections

def groupThePeople2(groupSizes):
    count = collections.defaultdict(list)
    for i, size in enumerate(groupSizes):
        count[size].append(i)
    return [l[i:i + s] for s, l in count.items() for i in range(0, len(l), s)]


p = [3,3,3,3,3,1,3]
p = [2,1,3,3,3,2]
p = [1]
print(groupThePeople(p))