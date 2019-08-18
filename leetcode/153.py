from typing import List
import unittest

class Solution:
	def findMin(self, nums: List[int]) -> int:
		l, r = 0, len(nums)-1
		while l<r:
			mid = int((l+r)/2)
			if nums[mid] > nums[r]:
				l = mid+1
			else:
				r = mid
		return nums[l]

class Testing(unittest.TestCase):

	def test_min(self):
		sol = Solution()
		cases = [
			[[3,4,5,1,2], 1],
			[[4,5,6,7,0,1,2], 0],
			[[3,1,2],0]
		]

		f1 = sol.findMin
		for i, x in enumerate(cases):
			self.assertEqual(f1(x[0]), x[1])

if __name__ == '__main__':
	unittest.main()