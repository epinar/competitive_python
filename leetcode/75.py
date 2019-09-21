

def sortColors(nums):
    '''
    Three pointers: left, right and zero. Also known as Dutch partitioning problem.
    '''
    l, r, zero = 0, len(nums)-1, 0
    while l <= r:
        if nums[l] == 0:
            nums[l], nums[zero] = nums[zero], nums[l]
            l += 1; zero += 1
        elif nums[l] == 2:
            nums[l], nums[r] = nums[r], nums[l]
            r -= 1
        else:
            l += 1
    return nums


def sortColors2(nums):
    '''
    Lomuto's algorithm. Two pointers, i is slow, for 0s and j is fast for 1s.
    '''
    i = j = 0
    for k in range(len(nums)):
        v = nums[k]
        nums[k] = 2
        if v != 2:
            nums[j] = 1
            j += 1
        if v == 0:
            nums[i] = 0
            i += 1
    return nums


if __name__ == '__main__':
    print(sortColors([2,0,2,1,1,0]))
    #print(sortColors([1, 0, 0]))