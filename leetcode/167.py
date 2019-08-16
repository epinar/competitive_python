from typing import List
import unittest

class Solution:
	def twoSum(self, numbers: List[int], target: int) -> List[int]:
		'''
		Two pointers showing the left and right search in the array.
		'''
		i, j = 0, len(numbers)-1
		while i<j:
			sum = numbers[i]+numbers[j]
			if sum == target:
				return i+1, j+1
			if sum < target:
				i+=1
			elif sum > target:
				j-=1

	def twoSum2(self, numbers: List[int], target: int) -> List[int]:
		'''
		Applies binary search to find the closest answer. Adds the solution
		to the dictionary to prevent collusion.
		'''
		dic = {}
		for i, num in enumerate(numbers):
			diff = target - num
			if diff in dic:
				return [i+1, dic[diff]+1]
			if diff not in dic:
				l, r = i+1, len(numbers)-1
				while l <= r:
					mid = int((l+r)/2)
					if numbers[mid] < diff:
						l = mid+1
					elif numbers[mid] > diff:
						r = mid-1
					else:
						return [i+1, mid+1]
				mid = int((l + r) / 2)
				dic[numbers[mid]] = mid


if __name__ == '__main__':
	sol = Solution()
	print(sol.twoSum2([2,7,11,15], 22))
	print(sol.twoSum2([0, 1, 3], 4))