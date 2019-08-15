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


if __name__ == '__main__':
	sol = Solution()
	#print(sol.longestCommonPrefix2(["a", "ac"]))
	#print(sol.longestCommonPrefix(["flower", "flow", "flight"]))
	unittest.main()
