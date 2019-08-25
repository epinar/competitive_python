from typing import List
import unittest

class Solution:
	def longestConsecutive(self, nums: List[int]) -> int:
		s = set(nums)
		res = 0

		for x in nums:
			if x-1 not in s:
				curr = 1
				curr_num = x
				while curr_num+1 in s:
					curr += 1
					curr_num +=1
				res = max(res, curr)
		return res

class Testing(unittest.TestCase):

	def test_min(self):
		sol = Solution()
		cases = [
			[[100, 4, 200, 1, 3, 2], 4]
		]

		f1 = sol.longestConsecutive
		for i, x in enumerate(cases):
			self.assertEqual(f1(x[0]), x[1])

if __name__ == '__main__':
	#unittest.main()
	sol = Solution()
	print(sol.longestConsecutive([100, 4, 200, 1, 3, 2]))