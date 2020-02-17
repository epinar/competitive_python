

def firstMissingPositive(nums):
    ## Find smallest missing positive integer

    mini = float("inf")
    for num in nums:
        if num>0:
            mini = num
            break

    for num in nums:
        if num>0 and num < mini:
            mini = num

    maxi = nums[0]
    for num in nums:
        if num>0 and num > mini:
            maxi = num

    if mini >1:
        return 1

    bin = [0]*(maxi-mini+1)
    for num in nums:
        if num >0:
            bin[num-mini] = 1

    for i, b in enumerate(bin):
        if b == 0:
            return (i+mini)

    return maxi+1

def firstMissingPositive2(nums):
    for i in range(len(nums)):
        while 0 <= nums[i]-1 < len(nums) and nums[nums[i]-1] != nums[i]:
            tmp = nums[i]-1
            nums[i], nums[tmp] = nums[tmp], nums[i]
            print(i, " : ",nums)
    for i in range(len(nums)):
        if nums[i] != i+1:
            return i+1
    return len(nums)+1

def firstMissingPositive3(nums):
    if not nums:
        return 1

    nums.append(0)
    l = len(nums)

    for i in range(l):
        if nums[i] <= 0 or nums[i] >= l:
            nums[i] = 0

    for i in range(l):
        nums[nums[i] % l] += l

        print(i, nums)

    for i in range(l):
        if not nums[i] // l:
            return i

    return l

def firstMissingPositive(nums) -> int:
    if not nums:
        return 1
    num_set = set(nums)
    for i in range(1, len(nums) + 2):
        if i not in num_set:
            return i

in1= [1, 2, 0]
in2 = [3, 4, -1, 1]
in3 = [7, 8, 9, 11, 12]
in4 = [0,1,2,4]
in5 = [3, 5, 7, 4, 2, 1]

print(firstMissingPositive3(in3))
