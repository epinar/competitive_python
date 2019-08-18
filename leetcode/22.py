from typing import List

class Solution:
	def generateParenthesis(self, n: int) -> List[str]:
		'''
		Recursively generate all possible parenthesis. For each open paranthesis,
		there must be a close paranthesis. At first, we have n opens at hand and
		we try to use them all. When all open&closed pars are left, we add the string
		to the result.
		'''

		def _generate(open, close, str, l=[]):
			if open == 0 and close == 0: l.append(str)
			if open > 0: _generate(open - 1, close + 1, str + "(", l)
			if close > 0: _generate(open, close - 1, str + ")", l)
			return l

		return _generate(n, 0, "")

	def generateParenthesis2(self, n: int) -> List[str]:
		'''
		Brute force solution, try all possible combinations and check
		if they are valid.
		'''

		res = []

		def is_valid(s):
			b = 0
			for c in s:
				if c == '(': b += 1
				else: b -= 1
				if b < 0: return False
			return b == 0

		def generate_all(curr=[]):
			if 2*n == len(curr):
				if is_valid(curr):
					res.append("".join(curr))
			else:
				curr.append('(')
				generate_all(curr)
				curr.pop()
				curr.append(')')
				generate_all(curr)
				curr.pop()

		generate_all()
		return res

	def generateParenthesis3(self, N):
		'''
		Considers a closure number c for each possible n, which are guaranteed
		to have ( at indice 0 and ) at 2*c+1. Then it adds the other valid
		sequences to indices between them.
		'''
		if N == 0: return ['']
		ans = []
		for c in range(N):
			for left in self.generateParenthesis(c):
				for right in self.generateParenthesis(N - 1 - c):
					ans.append('({}){}'.format(left, right))
		return ans

if __name__ == '__main__':
	sol = Solution()
	print(sol.generateParenthesis3(3))