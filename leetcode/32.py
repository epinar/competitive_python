import unittest

class Solution:

	def longestValidParentheses_1(self, s: str) -> int:
		'''

		We keep a starting index for the current substring.

		When we see a new open paranthesis ( , we update the current starting index,
		and add the previous one to the index list.

		When we see a closed paranthesis ) , if there is a matching ( , we take that
		from the list. This ( corresponds to the latest one we see. We take it's indice,
		calculate the length. Update the current starting index with the ( because our
		substring includes that.

		For a ) , if there are no ( in the list, then we update current start.

		'''
		max_count = 0
		start = []
		curr_start = 0
		for i, x in enumerate(s):
			if x == '(':
				start.append(curr_start)
				curr_start = i + 1
			elif x ==')' and start:
				curr_start = start.pop()
				count = i - curr_start + 1
				max_count = max(max_count, count)
			else:
				curr_start = i + 1

		return max_count

	def longestValidParentheses_2a(self, s: str) -> int:
		'''
		Iterate over the string to find the matching paranthesis through a stack.
		It there are elements left in the stack, they will indicate the interrupted sequences. Hence,
		the differences between their indices will show the lengths of the valid substrings. Be careful with
		tha last and the first indices!
		'''

		stack =[]
		for i, x in enumerate(s):
			if x == ')' and stack and s[stack[-1]] == '(':
				stack.pop()
			else:
				stack.append(i)

		if not stack:
			return len(s)

		max_count = 0
		stack.append(len(s))

		for i in range(len(stack)-1):
			count = stack[i+1] - stack[i] - 1
			max_count = max(max_count, count)

		max_count = max(max_count, stack[0])

		return max_count

	def longestValidParentheses_2b(self, s: str) -> int:
		'''
		A better version of solution2 is possible. We can traverse stack only 1 time to find the lengths.
		When we add a new element, the last element of the stack will show the longest valid sequence.
		If the stack is empty, it means that the substring was valid up to that point.
		To count up until last indice, we add a trivial character to the string.
		'''

		stack = []
		max_count = 0
		s+="0"
		for i, x in enumerate(s):
			if x == ')' and stack and s[stack[-1]] == '(':
				stack.pop()
			else:
				if stack:
					max_count = max(max_count, i - stack[-1]-1)
				else:
					max_count = max(max_count, i)
				stack.append(i)

		if not stack:
			return len(s)

		return max_count

	def longestValidParentheses_2c(self, s: str) -> int:
		'''
		Same solution to 2b, different words.
		'''

		stack = []
		max_count = 0
		stack.append(-1)
		for i, x in enumerate(s):
			if x == '(':
				stack.append(i)
			else:
				stack.pop()
				if stack:
					max_count = max(max_count, i-stack[-1])
				else:
					stack.append(i)
		return max_count


	def longestValidParentheses_3a(self, s: str) -> int:
		'''
		A natural dp approach to solve this problem. We keep the longest valid substring until each index we see.

		If the character is (, it means there are no valid substrings.
		If the character is ), there are two options:
			- ...()... which will immediately increase substring length by 2.
			- ...))... in this case we need to find the last ( seen, and increase the length by the previous
				max string length + 2.
		'''

		dp = []
		for i in range(len(s)):
			dp.append(0)
		max_count = 0
		for i in range(1, len(s)):
			if s[i] == ')':
				if s[i-1] == '(':
					dp[i] = (dp[i - 2] if i >= 2 else 0) + 2;
				if s[i-1] == ')':
					if (i - dp[i-1]>0) and s[i - dp[i-1] - 1] == '(':
						dp[i] = dp[i - 1] + (dp[i - dp[i - 1] - 2] if (i - dp[i - 1]) >= 2 else 0) + 2

				max_count = max(max_count, dp[i])
		return max_count


	def longestValidParentheses_3b(self, s: str) -> int:
		'''
		The same dynammic programming approach, put in different words.

		Update the dp array if ) is seen and there was at least 1 ( seen before.
			- Increase the length by 2.
			- Increase by the length of the previous valid substring.

		This was very similar to my first approach. Though I could not think of keeping a dp array. I was just keeping
		the prev longest length.

		'''

		dp = []
		for i in range(len(s)):
			dp.append(0)
		max_count = 0
		num_opens = 0
		for i in range(0, len(s)):
			if s[i] == '(':
				num_opens +=1
			elif s[i] == ')' and num_opens>0:
				dp[i] = 2 + dp[i-1]
				if i - dp[i] >0:
					dp[i] += dp[i-dp[i]]
				num_opens-=1
			max_count = max(max_count, dp[i])

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


class Testing(unittest.TestCase):

	def test_lengtht(self):
		sol = Solution()
		cases = [
			["(", 0],
			["()", 2],
			["())", 2],
			[")(", 0],
			["(()", 2],
			[")()())", 4],
			["(()(((()", 2],
			[")()())()()(", 4]
		]
		f1 = sol.longestValidParentheses_1
		for i, x in enumerate(cases):
			self.assertEqual(f1(x[0]), x[1])

		f2 = sol.longestValidParentheses_2a
		for i, x in enumerate(cases):
			self.assertEqual(f2(x[0]), x[1])

		f3 = sol.longestValidParentheses_2b
		for i, x in enumerate(cases):
			self.assertEqual(f3(x[0]), x[1])

		f32 = sol.longestValidParentheses_2c
		for i, x in enumerate(cases):
			self.assertEqual(f32(x[0]), x[1])

		f4 = sol.longestValidParentheses_3a
		for i, x in enumerate(cases):
			self.assertEqual(f4(x[0]), x[1])

		f5 = sol.longestValidParentheses_3b
		for i, x in enumerate(cases):
			self.assertEqual(f5(x[0]), x[1])


if __name__ == '__main__':

	s = ")()())"
	s = "(()(((()"

	s = ")()())()()("
	s = ")("
	sol = Solution()

	unittest.main()
