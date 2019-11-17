
t = int(input())

for _ in range(t):
    n = int(input())
    a = list(map(int, input().split()))
    m = int(input())
    h = [tuple(map(int, input().split())) for i in range(m)]
    h.sort(reverse=True)
    print(h)
    new_h = []
    prev = 0
    for p, s in h:
        if s > prev:
            new_h.append((p, s))
            prev = s

    h = new_h
    hum = 0
    res = 1
    cur = 0
    maxp = 0
    for mon in a:
        maxp = max(mon, maxp)
        cur += 1
        if mon > h[0][0]:
            res = -1
            break
        if hum < len(h) and cur > h[hum][1]:
            hum += 1
        if hum == len(h) or maxp > h[hum][0]:
            res += 1
            hum = 0
            cur = 1
            maxp = mon

    print(res)