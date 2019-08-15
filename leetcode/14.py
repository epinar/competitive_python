from typing import List
import unittest


class Solution:
	def longestCommonPrefix(self, strs: List[str]) -> str:
		'''
		Vertically check the characters for each string in the list. When the
		condition is broken or the limits are exceeded, return the result.
		'''
		if len(strs) == 0:
			return ""
		i = 0
		n = len(strs)
		lens = [len(x) for x in strs]
		for x in lens:
			if x == 0:
				return ""
		min_len = min(lens)
		res = ""
		while i < min_len:
			ch = strs[0][i]
			for j in range(1, n):
				if i == len(strs[j]):
					return res
				if ch != strs[j][i]:
					return res
			res += ch
			i += 1
		return res

	def longestCommonPrefix2(self, strs: List[str]) -> str:
		'''
		Trie is a string tree built from a list of strings. The nodes point to
		the common prefix of the child nodes. We first build the trie, then find
		the last node that has 1 child node.
		'''

		res = ""
		if len(strs) == 0:
			return res
		trie_root = self.make_trie(strs)

		while len(trie_root) == 1:
			k = list(trie_root.keys())[0]
			if k == '_end':
				break
			trie_root = trie_root[k]
			res += k

		return res

	def make_trie(self, words: List[str]):
		_end = '_end'
		root = {}
		for word in words:
			current_dict = root
			for letter in word:
				current_dict = current_dict.setdefault(letter, {})
			current_dict[_end] = _end
		return root

	def longestCommonPrefix3(self, strs: List[str]) -> str:
		'''
		Sorts the strings in an alphabetic order, then compares the min
		and max element. All the prefixes common in both of them
		automatically occur in the other strings in middle.
		'''

		if not strs:
			return ""

		s1 = min(strs)
		s2 = max(strs)

		for i, c in enumerate(s1):
			if c != s2[i]:
				return s1[:i]  # stop until hit the split index
		return s1

	def longestCommonPrefix4(self, strs: List[str]) -> str:
		'''
		Same with the first vertical solution, though makes use of
		python's zip+enumerate. Takes the i indexed character of all
		strings, checks if they are all same.
		'''

		if not strs:
			return ""

		for i, letter_group in enumerate(zip(*strs)):
			if len(set(letter_group)) > 1:
				return strs[0][:i]
		else:
			return min(strs)

	def longestCommonPrefix5(self, strs: List[str]) -> str:
		'''
		Divides the list to two parts, searches in them until
		there are two strings to compare. Then, the common prefix
		of these two strings are sent to higher level, which is
		again get compared with another prefix to select out the
		common part.
		'''
		if not strs:
			return ""
		return self._lcp(strs, 0, len(strs) - 1)

	def _lcp(self, strs, l, r):
		if l == r:
			return strs[l]
		else:
			mid = int((l+r)/2)
			left = self._lcp(strs, l, mid)
			right = self._lcp(strs, mid+1, r)
			return self._cp(left, right)

	def _cp(self, str1, str2):
		min_len = min(len(str1), len(str2))
		for i in range(min_len):
			if str1[i]!=str2[i]:
				return str1[:i]

		return str1[:min_len]

	def longestCommonPrefix6(self, strs: List[str]) -> str:
		'''
		Applies binary search starting from the minimum length
		string. Divides the string, checks if the first half occurs
		in all other strings.
		'''
		if not strs:
			return ""
		lens = [len(x) for x in strs]
		min_len = min(lens)
		low = 1
		high = min_len
		while low <= high:
			mid = int((low+high)/2)
			if self._iscp(strs, mid):
				low = mid + 1
			else:
				high = mid - 1
		return strs[0][:int((low+high)/2)]

	def _iscp(self, strs, mid):
		mid_str = strs[0][:mid]
		for x in strs:
			if x[:mid] != mid_str:
				return False
		return True

class Testing(unittest.TestCase):

	def test_prefix(self):
		sol = Solution()
		cases = [
			[["flower", "flow", "flight"], "fl"],
			[["dog", "racecar", "car"], ""],
			[["ada", "ada", "ada"], "ada"],
			[["ada", "ada", "adb"], "ad"],
			[["a", "b", ""], ""],
			[["","b"], ""],
			[["a", "ac"], "a"]
		]

		f1 = sol.longestCommonPrefix
		for i, x in enumerate(cases):
			self.assertEqual(f1(x[0]), x[1])

		f2 = sol.longestCommonPrefix2
		for i, x in enumerate(cases):
			self.assertEqual(f2(x[0]), x[1])

		f3 = sol.longestCommonPrefix3
		for i, x in enumerate(cases):
			self.assertEqual(f3(x[0]), x[1])

		f4 = sol.longestCommonPrefix4
		for i, x in enumerate(cases):
			self.assertEqual(f4(x[0]), x[1])

		f5 = sol.longestCommonPrefix5
		for i, x in enumerate(cases):
			self.assertEqual(f5(x[0]), x[1])

		f6 = sol.longestCommonPrefix6
		for i, x in enumerate(cases):
			self.assertEqual(f6(x[0]), x[1])


if __name__ == '__main__':
	sol = Solution()
	#print(sol.longestCommonPrefix3(["a", "ac"]))
	#print(sol.longestCommonPrefix6(["flower", "flow", "flight"]))
	unittest.main()
