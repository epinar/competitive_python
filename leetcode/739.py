

def dailyTemperatures(T):

    N = len(T)
    res = [0]*N
    h = []
    for i in range(N-1, -1, -1):
        while h and T[h[-1]] <= T[i]:
            h.pop()
        res[i] = h[-1] - i if h else 0
        h.append(i)
    return res

def dailyTemperatures2(T):

    res = [0]*len(T)
    s = []
    for i, val in enumerate(T):
        while s and T[s[-1]] < val:
            cur = s.pop()
            res[cur] = i - cur
        s.append(i)
    return res


if __name__ == '__main__':

    print(dailyTemperatures2([73, 73, 75, 71, 69, 72, 76, 73]))