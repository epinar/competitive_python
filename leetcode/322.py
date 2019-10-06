
def coinChange(coins, amount):
    if amount < 1: return 0
    # coins = sorted(coins)[::-1]

    dp = [0] * (amount + 1)

    def isPossible(rem):
        if rem < 0: return -1
        if rem == 0: return 0
        if dp[rem]: return dp[rem]
        min = float("inf")
        for i in range(len(coins)):
            # print("  try ", coins[i])
            k = isPossible(rem - coins[i])
            if k >= 0 and k < min:
                min = k + 1
        dp[rem] = -1 if min == float("inf") else min
        return dp[rem]

    return isPossible(amount)


def coinChange2(coins, amount):
    dp = [0] + [amount +1 ] *(amount)

    for a in range(1, amount +1):
        for c in coins:
            if c <= a:
                dp[a] = min(dp[a], dp[ a -c ] +1)


    return dp[-1] if dp[-1] != amount +1 else -1



if __name__ == '__main__':
    coins = [186, 419, 83, 408]
    amount = 6249
    # coins = [1, 2, 5]
    # amount = 11
    print(coinChange(coins, amount))
    print(coinChange([2], 3))
