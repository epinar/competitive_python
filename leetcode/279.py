

def numSquares(n: int) -> int:

    if n < 2:
        return n

    l = []
    for i in range(1, n):
        if i*i > n:
            break
        l.append(i*i)

    q = {n}
    res = 0
    while len(q) > 0:
        res += 1
        next_q = set()
        for i in q:
            for j in l:
                print("rem: ", i, " square: ", j)
                if i == j:
                    return res
                if i < j:
                    break
                next_q.add(i-j)

        q = next_q

    return res

def numSquares2(n):
    dp = [0] * (n + 1)
    for i in range(1, n + 1):
        l = []
        for j in range(1, int(i ** .5) + 1):
            l.append(dp[i - j*j])
        dp[i] = min(l)+1
    return dp[n]

def numSquares3(n):
    '''
    Same thing shorter.
    '''
    dp = [0] * (n + 1)
    for i in range(1, n + 1):
        dp[i] = min([dp[i - j * j] for j in range(1, int(i ** .5) + 1)]) + 1
    return dp[n]


if __name__ == '__main__':
    print(numSquares2(12))