from typing import List
import unittest

class Solution:

	def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:

		'''
		This is a very elegant solution. We try to split both the lists such that
		they have equal elements in total, and the maximum of the left part is
		smaller than the minimum of the right part.

		i points to the splitting place on first array, j points the second. We
		aim to find the positions of i and j. i+j is the middle of all elements.

		imin, imax defines the range we search for i. j is automatically the point
		that makes i+j middle, st. (m+n+1)/2.

		Stopping criteria is that nums1[i-1]<nums2[j] and nums2[j-1]<nums1[i].


		'''

		m, n = len(nums1), len(nums2)
		if m > n:
			m , n = n, m
			nums1, nums2 = nums2, nums1

		imin, imax = 0, m
		while imin <= imax:
			i = (imin+imax)//2
			j = (m+n+1)//2-i

			if i<m and nums2[j-1] > nums1[i]:
				imin = i + 1
			elif i>0 and nums1[i-1] > nums2[j]:
				imax = i - 1
			else:
				if i == 0:
					left = nums2[j-1]
				elif j == 0:
					left = nums1[i-1]
				else:
					left = max(nums1[i-1], nums2[j-1])

				if (m + n) % 2 == 1:
					return left

				if i == m:
					right = nums2[j]
				elif j == n:
					right = nums1[i]
				else:
					right = min(nums1[i], nums2[j])

				return (left+right)/2

	def findMedianSortedArrays2(self, nums1: List[int], nums2: List[int]) -> float:

		'''
		This is the same solution with above, written with recursion. Instead of
		keeping mini and maxi, which helps keeping the search range of i and j,
		we crop out the arrays from i or j and search in them.
		Base cases are handled out such that:
			- If the first array is empty, we return kth from the second one.
			- If k is equal to total sum of arrays, return the maximum last value.
		'''

		tot = len(nums1)+ len(nums2)
		if tot%2 == 1:
			return self._findKthSmallest(nums1, nums2, tot//2)
		else:
			return (self._findKthSmallest(nums1, nums2, tot//2-1)+self._findKthSmallest(nums1, nums2, tot//2))/2

	def _findKthSmallest(self, nums1, nums2, k):

		m, n = len(nums1), len(nums2)
		if m > n:
			m, n = n, m
			nums1, nums2 = nums2, nums1

		if not nums1:
			return nums2[k]
		if k == m+n-1:
			return max(nums1[-1], nums2[-1])

		i = m//2
		j = k-i
		if nums1[i]>nums2[j]:
			return self._findKthSmallest(nums1[:i], nums2[j:], i)
		else:
			return self._findKthSmallest(nums1[i:], nums2[:j], j)

class Testing(unittest.TestCase):

	def test_median(self):
		sol = Solution()
		cases = [
			[[1], [1], 1],
			[[1, 3], [2], 2],
			[[1, 2], [3, 4], 2.5]
		]
		f1 = sol.findMedianSortedArrays
		for i, x in enumerate(cases):
			self.assertEqual(f1(x[0], x[1]), x[2])

		f2 = sol.findMedianSortedArrays2
		for i, x in enumerate(cases):
			self.assertEqual(f2(x[0], x[1]), x[2])

if __name__ == '__main__':

	unittest.main()