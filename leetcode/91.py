

def numDecodings(s):
    # Recursion solution with memoization

    mem = {}

    def decode(i):
        # print('i: ', i)
        if len(s) == 0 or int(s[0]) == 0:
            return 0
        if i >= len(s):
            return 1

        a, b = 0, 0
        if int(s[i]) > 0:
            if s[i+1:] in mem:
                a = mem[s[i+1:]]
            else:
                a = decode(i + 1)
        if i + 1 < len(s):
            # print(int(s[i]+s[i+1]))
            if 0 < int(s[i] + s[i + 1]) <= 26 and int(s[i]) > 0:
                if s[i+2:] in mem:
                    b = mem[s[i+2:]]
                else:
                    b = decode(i + 2)
        mem[s[i:]]= a+b
        # print(a, b)
        return a + b

    return decode(0)

def numDecodings2(s):
    # DP solution
    if not s:
        return 0

    dp = [0 for _ in range(len(s)+1)]
    dp[0] = 1
    dp[1] = 1 if s[0] != '0' else 0
    print(dp)

    for i in range(2, len(s)+1):
        print("i ", i)
        if s[i-1] != '0':
            dp[i] += dp[i-1]
            print("one: ", dp)
        if s[i-2] != '0' and int(s[i-2]+s[i-1]) <=26:
            dp[i] += dp[i-2]
            print("two: ", dp)

    print(dp)
    return dp[-1]

def numDecodings3(s):
    # dp with less memory
    if not s:
        return 0

    pprev = 1
    prev = 1 if s[0] != '0' else 0

    for i in range(2, len(s) + 1):
        print("i ", i)
        temp = 0
        if s[i - 1] != '0':
            temp += prev
            print("one: ", prev)
        if s[i - 2] != '0' and int(s[i - 2] + s[i - 1]) <= 26:
            temp += pprev
            print("two: ", pprev)

        pprev, prev = prev, temp

    return prev

s= '226'
print(numDecodings3(s))