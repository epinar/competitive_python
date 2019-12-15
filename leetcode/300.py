

def lengthOfLIS(nums):

    cts = [1]
    for i in range(1, len(nums)):
        ops = [0]
        for j in range(i):
            if nums[i] >= nums[j]:
                ops.append(cts[j])
        cts.append(max(ops)+1)
    return max(cts)

def lengthOfLIS2(nums):
    from bisect import bisect_left
    dp = [0]*len(nums)
    res = 0
    for i in range(len(nums)):
        j = bisect_left(dp, nums[i], hi=res)
        dp[j] = nums[i]
        res = max(j+1, res)
    return res

def lengthOfLIS3(nums):
    tails = [0] * len(nums)
    size = 0
    for x in nums:
        i, j = 0, size
        while i != j:
            m = (i + j) // 2
            if tails[m] < x:
                i = m + 1
            else:
                j = m
        tails[i] = x
        print(i, " ", tails)
        size = max(i + 1, size)
    return size

lis = [10,9,2,5,3,7,101,18]
lis = [10, 4, 5, 2, 1, 7]
lis = [0, 8, 4, 12]
lis = [1]
print(lengthOfLIS2(lis))