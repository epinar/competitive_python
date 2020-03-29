
from copy import copy

def getKth(lo, hi, k):

    nums = {}
    for i in range(lo, hi+1):
        x = copy(i)
        if x not in nums:
            curr = 0
            while x != 1:
                if x % 2 == 0:
                    x = x/2
                else:
                    x = 3*x+1
                curr += 1
                if x in nums:
                    curr += nums[x]
                    break
            nums[i] = curr
    sorted_nums = sorted(nums.items(), key=lambda nums: (nums[1],nums[0]))
    return sorted_nums[k-1][0]

print(getKth(12,15,2))

#print(getKth(1,1,1))

#print(getKth(10,20,5))

print(getKth(1,1000,777))




