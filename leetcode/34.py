
def searchRange(nums, target):

    if len(nums) == 0:
        return [-1, -1]

    l, r = 0, len(nums)
    mid = int((l + r) / 2)

    while l < r:
        if nums[mid] < target:
            l = mid+1
        elif nums[mid] > target:
            r = mid
        else:
            break
        mid = int((l + r) / 2)

    if nums[mid] != target:
        return [-1, -1]

    l, r = mid, mid
    while l > 0 and nums[l-1] == target:
        l -= 1

    while r < len(nums)-1 and nums[r+1] == target:
        r += 1

    return [l, r]

def searchRange2(nums, target):

    if len(nums) == 0:
        return [-1, -1]

    l, r = 0, len(nums)-1

    while l < r:
        mid = (l + r) // 2
        if nums[mid] < target:
            l = mid+1
        else:
            r = mid

    if nums[l] != target:
        return [-1, -1]

    left = l
    l, r = left, len(nums)-1
    while l < r:
        m = (l+r)//2 + 1
        if nums[m] == target:
            l = m
        else:
            r = m-1
    right = l
    return [left, right]

if __name__ == '__main__':
    print(searchRange2([5,7,7,8,8,10], 5))
    print(searchRange2([1,1,1], 1))
    print(searchRange2([], 1))