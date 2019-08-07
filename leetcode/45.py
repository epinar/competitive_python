import sys
from typing import List
import unittest

class Solution:

	def jump(self, nums: List[int]) -> int:
		'''
		We keep the furthest point in reach in variable curr, and the previous
		furthest one in the prev. Then we check the points in between, decide
		the next furthest point in reach, update the curr and prev accordingly.
		Stop the iteration at the first time we hit the last index.
		'''
		if len(nums) == 1:
			return 0
		prev = 0
		curr = nums[0]
		steps = 1
		while curr < len(nums)-1:
			furthest = curr
			for j in range(prev, curr+1):
				furthest = max(nums[j] + j, furthest)
			prev = curr
			curr = furthest
			steps +=1
		return steps


	def jump2(self, nums: List[int]) -> int:
		'''
		Similar solution. Now, assume that we did not even see the first point.
		We need to keep the indice for traversal.
		'''
		prev = 0
		curr = 0
		steps = 0
		i = 0
		while curr < len(nums) - 1:
			while i <= prev:
				curr = max(nums[i] + i, curr)
				i += 1
			prev = curr
			steps += 1
		return steps

class Testing(unittest.TestCase):

	def test_jump(self):
		sol = Solution()
		cases = [
			[[2, 3, 1, 1, 4], 2],
			[[1, 1, 1, 1], 3],
			[[2, 1], 1],
			[[1, 2, 3], 2],
			[[2, 3, 1], 1],
			[[0], 0],
			[[5, 9, 3, 2, 1, 0, 2, 3, 3, 1, 0, 0], 3]
		]
		f1 = sol.jump
		for i, x in enumerate(cases):
			self.assertEqual(f1(x[0]), x[1])

		f2 = sol.jump2
		for i, x in enumerate(cases):
			self.assertEqual(f2(x[0]), x[1])

if __name__ == '__main__':

	unittest.main()