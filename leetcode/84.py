from typing import List
import unittest


class Solution:
	def largestRectangleArea(self, heights: List[int]) -> int:
		'''
		Primitive solution that iterates over the heights and all possible
		combinations, returns the maximum size.
		'''
		res, curr = 0, 0
		N = len(heights)
		for i in range(N):
			mini = heights[i]
			curr = mini * 1
			res = max(res, curr)
			for j in range(i + 1, N):
				mini = min(mini, heights[j])
				curr = mini * (j - i + 1)
				res = max(res, curr)
		return res

	def largestRectangleArea2(self, heights: List[int]) -> int:
		'''
		For each bar, expands from left and right to get the largest possible
		rectangle, returns the max.
		'''
		res, curr = 0, 0
		N = len(heights)
		lefts, rights = [1] * N, [1] * N
		for i in range(N):
			left = i-1
			while left >= 0 and heights[left] >= heights[i]:
				lefts[i] += lefts[left]
				left -= lefts[left]

		for i in range(N-1, -1, -1):
			right = i+1
			while right < N and heights[right] >= heights[i]:
				rights[i] += rights[right]
				right += rights[right]

		for i in range(N):
			curr = (rights[i] + lefts[i] - 1) * heights[i]
			res = max(res, curr)
		return res

	def largestRectangleArea3(self, heights: List[int]) -> int:
		'''
		Use a stack to keep the heights. At each bar, calculate the maximum possible rectangle
		formed by the previous higher bars, and remove the higher bars from the stack.
		'''
		heights.append(0)
		s = [-1]
		res, curr = 0, 0
		N = len(heights)
		for i in range(N):
			while heights[i] < heights[s[-1]]:
				h = heights[s.pop()]
				w = i - s[-1] - 1
				curr = h*w
				res = max(curr, res)
			s.append(i)
		return res


class Testing(unittest.TestCase):

	def test_min(self):
		sol = Solution()
		cases = [
			[[2, 1, 5, 6, 2, 3], 10],
			[[2], 2],
			[[2, 2], 4],
			[[2, 2, 1], 4],
			[[2, 1, 2], 3]
		]

		f1 = sol.largestRectangleArea
		for i, x in enumerate(cases):
			self.assertEqual(f1(x[0]), x[1])

		f2 = sol.largestRectangleArea2
		for i, x in enumerate(cases):
			self.assertEqual(f2(x[0]), x[1])

		f3 = sol.largestRectangleArea3
		for i, x in enumerate(cases):
			self.assertEqual(f3(x[0]), x[1])


if __name__ == '__main__':
	#unittest.main()
	sol = Solution()
	print(sol.largestRectangleArea2([2, 1, 2]))
	#print(sol.largestRectangleArea([2, 2, 1]))
