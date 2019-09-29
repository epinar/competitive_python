

def subarraySum(nums, k):

    N = len(nums)
    sums = {}
    sums[0] = 1
    ans = 0
    s = 0
    for i in range(N):
        s += nums[i]
        if s-k in sums:
            ans += sums[s-k]
        if s in sums:
            sums[s] += 1
        else:
            sums[s] = 1

    return ans


if __name__ == '__main__':
    print(subarraySum([1, 1, 1, 0, 1, 1], 2))
    #print(subarraySum([1], 0))