
def findDuplicate(nums):
    # Find the intersection point of the two runners.
    tortoise = nums[0]
    hare = nums[0]
    while True:
        tortoise = nums[tortoise]
        hare = nums[nums[hare]]
        if tortoise == hare:
            break
    ptr1 = nums[0]
    ptr2 = tortoise
    while ptr1 != ptr2:
        ptr1 = nums[ptr1]
        ptr2 = nums[ptr2]

    return ptr1

def findDuplicate2(nums):
    nums.sort()
    for i in range(1, len(nums)):
        if nums[i] == nums[i - 1]:
            return nums[i]

if __name__ == '__main__':
    print(findDuplicate([1,2,3,1]))
    print(findDuplicate([2, 2, 2, 2]))
    print(findDuplicate([2,5,9,6,9,3,8,9,7,1]))