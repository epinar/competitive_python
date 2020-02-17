

## UNSOLVED!!!
def maxProduct(nums):

    big, sml = nums[0], nums[0]
    max = nums[0]


    for i in range(1, len(nums)):

        if nums[i]<0:

        if nums[i]*big > big:
            pos = pos * nums[i]

        if nums[i]*neg < neg:
            neg = neg * nums[i]
        elif nums[i] < neg:
            neg = nums[i]

    if curr > res:
        res = curr

    return res

#print(maxProduct([2, 3, -2, 4]))
#print(maxProduct([-2, 0, -1]))
print(maxProduct([-2, 3, -4]))