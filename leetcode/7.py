
import unittest

class Solution:
	def reverse(self, x: int) -> int:
		'''
		divmod divides the element and returns the remainder as mod.
		'''

		k = 0
		n = [1, -1][x<0]
		x = abs(x)
		while x != 0:
			x, mod = divmod(x, 10)
			k = k*10 + mod
		return n * k if -pow(2, 31) <= n * k <= pow(2, 31) - 1 else 0

	def reverse2(self, x: int) -> int:
		'''
		This one uses the python's list reversing function [::-1].
		'''
		s = (x > 0) - (x < 0)
		r = int(str(x * s)[::-1])
		return s * r * (r < 2 ** 31)


class Testing(unittest.TestCase):

	def test_reverse(self):
		sol = Solution()
		cases = [
			[123, 321],
			[-123, -321],
			[120, 21]
		]

		f1 = sol.reverse
		for i, x in enumerate(cases):
			self.assertEqual(f1(x[0]), x[1])

		f2 = sol.reverse2
		for i, x in enumerate(cases):
			self.assertEqual(f2(x[0]), x[1])


if __name__ == '__main__':

	unittest.main()