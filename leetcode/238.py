
from typing import List

def productExceptSelf(nums: List[int]) -> List[int]:
    res = [1]*len(nums)

    prev = 1
    for i in range(len(nums)):
        res[i] = prev
        prev = nums[i]*prev

    prev = 1
    for i in range(len(nums)-1, -1, -1):
        res[i] = res[i]*prev
        prev = nums[i]*prev

    return res


if __name__ == '__main__':
    print(productExceptSelf([1, 2, 3, 4]))