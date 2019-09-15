

def maxCoins1(nums):
    '''
    This is the most straightforward solution that would stuck at time limit.
    '''

    all_res = []
    def burst(i, rem, res):
        if len(rem) == 1:
            all_res.append(res+rem[0])
            return
        if i == 0:
            res = res + rem[i] * rem[i+1]
        elif i == len(rem)-1:
            res = res + rem[i] * rem[i-1]
        else:
            res = res + rem[i-1] * rem[i] * rem[i+1]
        rem.pop(i)
        for j in range(len(rem)):
            burst(j, rem.copy(), res)

    for i, n in enumerate(nums):
        burst(i, nums.copy(), 0)

    return max(all_res)


def maxCoins2(nums):
    '''
    Top-down solution to speed things up.
    Assume we have burst n-2 baloons and left with the outermost baloons,
    which are 0 and n-1 th. Now, build the solution by traversing backwards.
    Calculate the value for the last burst baloon, and so on by divide and conquer.
    '''

    nums.insert(0, 1)
    nums.append(1)
    n = len(nums)
    dp = [[0]*n for _ in range(n)]

    def burst(l, r):
        if l+1 == r:
            return 0
        if dp[l][r] > 0:
            return dp[l][r]
        ans = 0
        for i in range(l+1, r):
            ans = max(ans, nums[l]*nums[i]*nums[r] + burst(l, i) + burst(i, r))
        dp[l][r] = ans
        return ans

    return burst(0, n-1)


def maxCoins3(nums):
    '''
    This is the bottom-up solution, the idea is similar to previous one.
    Instead of recursing backwards, build the solution from the smallest pieces.
    '''
    nums.insert(0, 1)
    nums.append(1)
    n = len(nums)
    dp = [[0] * n for _ in range(n)]

    for k in range(2, n):
        for left in range(0, n-k):
            right = left+k
            for i in range(left+1, right):
                dp[left][right] = max(dp[left][right], nums[left]*nums[i]*nums[right]+dp[left][i]+dp[i][right])

    return dp[0][n-1]



if __name__ == '__main__':
    print(maxCoins2([3,1,5,8]))

    print(maxCoins3([3,1,5,8]))