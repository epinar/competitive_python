from typing import List
import unittest

class Solution:
	def searchInsert(self, nums: List[int], target: int) -> int:

		l, r = 0, len(nums)

		while l < r:
			mid = (int)((l+r)/2)
			if nums[mid] == target:
				return mid
			elif nums[mid] > target:
				r = mid - 1
			else:
				l = mid + 1

		return (int)((l+r)/2)


class Testing(unittest.TestCase):

	def test_min(self):
		sol = Solution()
		cases = [
			[[1,3,5,6], 5, 2],
			[[1, 3, 5, 6], 2, 1],
			[[1, 3, 5, 6], 7, 4],
			[[1, 3, 5, 6], 0, 0]
		]

		f1 = sol.searchInsert
		for i, x in enumerate(cases):
			self.assertEqual(f1(x[0], x[1]), x[2])


if __name__ == '__main__':
	unittest.main()
	sol = Solution()
	print(sol.searchInsert([1, 3], 1))