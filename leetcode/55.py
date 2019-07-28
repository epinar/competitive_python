from typing import List
import unittest

class Solution:

	def canJump(self, nums: List[int]) -> bool:
		'''
		We traverse through the array from left to right and try to reach the
		furthest point at each iteration. If we can reach the last point, return
		true.
		'''
		rem = 0
		for i, x in enumerate(nums):
			if rem < i: return False
			if rem >= len(nums)-1: return True
			rem = max(rem, i+x)

	def canJump2(self, nums: List[int]) -> bool:
		'''
		Now, traverse from right to left, and check if the current point is reachable
		from the left neighbor. Similar logic with the previous solution, but this
		one traverses the whole array, whereas the former stops once it becomes sure.
		'''
		last = len(nums)-1
		for i in range(len(nums)-1):
			ind = len(nums)-i-2
			if ind + nums[ind] >= last:
				last = ind
		return last==0

class Testing(unittest.TestCase):

	def test_jump(self):
		sol = Solution()
		true_cases = [
			[2, 3, 1, 1, 4],
			[1, 1, 1, 1],
			[2, 1],
			[1, 2, 3],
			[2, 3, 1],
			[0]
		]
		false_cases = [
			[3, 2, 1, 0, 4],
			[0, 1]
		]
		f1 = sol.canJump
		for i, x in enumerate(true_cases):
			self.assertTrue(f1(x))

		for i, x in enumerate(false_cases):
			self.assertFalse(f1(x))

		f2 = sol.canJump
		for i, x in enumerate(true_cases):
			self.assertTrue(f2(x))

		for i, x in enumerate(false_cases):
			self.assertFalse(f2(x))

if __name__ == '__main__':

	unittest.main()
