
def minimize(s, n, k):

    s = list(s)
    fin = False
    cnt = 0
    i = 0
    res = ''
    while i < n:
        if s[i] == '1':
            cnt += 1
        else:
            if cnt < k:
                k -= cnt
                res += '0'
            else:
                fin = True
                for j in range(cnt-k):
                    res += '1'
                res += '0'
                for j in range(k):
                    res += '1'
                res += "".join(s[i+1:])
                break
        i += 1

    if not fin:
        for i in range(cnt):
            res += '1'
            i += 1

    return res

if __name__ == '__main__':

    #print(minimize('1111100', 7, 11))
    #exit()

    q = int(input())
    for i in range(q):
        n, k = map(int, input().split())
        s = input()
        res = minimize(s, n, k)
        print(res)