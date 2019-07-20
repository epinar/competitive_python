

class Solution:

	def longestValidParentheses_1(self, s: str) -> int:

		max_count = 0
		start = []
		prev_start = 0
		for i, x in enumerate(s):
			if x == '(':
				start.append(prev_start)
				prev_start = i
			elif x ==')' and len(start):
				prev_start = start.pop()
				count = i - prev_start
				max_count = max(max_count, count)
			else:
				prev_start = i

		return max_count

	def longestValidParentheses_2(self, s: str) -> int:

		max_count = 0
		start = []
		prev_start = 0
		for i, x in enumerate(s):
			if x == '(':
				start.append(prev_start)
				prev_start = i
			elif x ==')' and len(start):
				prev_start = start.pop()
				count = i - prev_start
				max_count = max(max_count, count)
			else:
				prev_start = i

		return max_count

	def longestValidParentheses_3(self, s: str) -> int:

		max_count = 0
		start = []
		prev_start = 0
		for i, x in enumerate(s):
			if x == '(':
				start.append(prev_start)
				prev_start = i
			elif x ==')' and len(start):
				prev_start = start.pop()
				count = i - prev_start
				max_count = max(max_count, count)
			else:
				prev_start = i

		return max_count

	def isValid(self, s: str) -> bool:
	# Returns true if it is valid
		num_opens = 0
		for i in range(len(s)):
			c = s[i]
			if c == '(':
				num_opens+=1
			elif c == ')':
				if num_opens<1:
					return False
				else:
					num_opens-=1
		if num_opens == 0:
			return True
		else:
			return False

	def isValid2(self, s: str) -> bool:
		stack = []
		for i in range(len(s)):
			c = s[i]
			if c in ["(", "[", "{"]:
				stack.append(c)
			else:
				last = stack.pop()
				if (c ==")" and last=="(") or (c =="]" and last=="[") or (c =="}" and last=="{"):
					continue
				else:
					return False

		return len(stack)==0


if __name__ == '__main__':

	s = ")()())"
	s="(()(((()"
	#s = "(()"

	s=")()())()()("
	s = ")()"
	sol = Solution()
	print(sol.longestValidParentheses(s))

	#s = "(){}[]"
	#print(sol.isValid2(s))