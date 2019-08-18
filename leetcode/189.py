from typing import List
import unittest


class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        '''
        Brute force solution, exceeds time limit.
        '''
        if len(nums) == 1:
            return
        if k >= len(nums):
            k = k%len(nums)

        for i in range(k):
            self._rotateOnce(nums)

    def _rotateOnce(self, nums: List[int]):
        last = nums[-1]
        j = len(nums)-1
        while j>0:
            nums[j] = nums[j-1]
            j -= 1
        nums[0] = last

    def rotate2(self, nums: List[int], k: int) -> None:
        '''
        Reverse the elements three times.
        '''

        k, n = k % len(nums), len(nums)
        if k:
            self._numReverse(0, nums, n - 1)
            self._numReverse(0, nums, k - 1)
            self._numReverse(k, nums, n - 1)

    def _numReverse(self, start, nums, end):
        """
        Reverses an array from start to end. It is also possible
        to use [::-1] function of python.
        """
        while start < end:
            nums[start], nums[end] = nums[end], nums[start]
            start += 1
            end -= 1

    def rotate3(self, nums, k):
        k = k % len(nums)
        nums[:] = nums[-k:] + nums[:-k]


if __name__ == '__main__':
    sol = Solution()
    arr = [-1, -100, 3, 99]
    arr = [1, 2, 3, 4]
    arr = [1, 2, 3, 4, 5, 6]
    print(arr[::-1])
    sol.rotate3(arr, 1)
    print(arr)
