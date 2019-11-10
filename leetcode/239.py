
import heapq
import collections


def maxSlidingWindow1(nums, k):
    '''
    Straightforward approach.
    '''
    if len(nums) == 0:
        return None
    i = 0
    j = k - 1
    res = []
    while i < len(nums) - k + 1 and j < len(nums):
        max_win = max(nums[i:j + 1])
        res.append(max_win)
        i += 1
        j += 1
    return res

def maxSlidingWindow2(nums, k):
    '''
    Keep the elements with their indices in a heap. Retrieve/modify heap for each window slide.
    '''

    if len(nums) == 0 or k == 0:
        return []
    if len(nums) < k:
        return [max(nums)]

    res = []
    h = []
    for i in range(k):
        heapq.heappush(h, (-nums[i], i))
    res.append(-h[0][0])

    for i in range(k, len(nums)):
        heapq.heappush(h, (-nums[i], i))

        # Get the maximum element.
        el = heapq.heappop(h)
        while el[1] <= i-k:
            el = heapq.heappop(h)

        heapq.heappush(h, el) # Put the element back.
        res.append(-el[0])

    return res

def maxSlidingWindow2_b(nums, k):
    '''
    Same solution with elegant code :)
    '''
    res = []
    h = []
    for i in range(len(nums)):
        while h and h[0][1] < i - k + 1:
            heapq.heappop(h)
        heapq.heappush(h, (-nums[i], i))
        if i >= k - 1:
            res.append(-h[0][0])
    return res

def maxSlidingWindow3(nums, k):
    '''
    Keep the window values in a deque (double-ended queue). At each step,
        1. Remove the smaller elements in the deque, start from last indices.
        2. Remove the elements out of window, check the initial indice of the array.
    '''
    candidates = collections.deque()
    res = []
    for i, num in enumerate(nums):
        while candidates and candidates[-1][0] <= num:
            candidates.pop()
        while candidates and candidates[0][1] < i - k + 1:
            candidates.popleft()
        candidates.append((num, i))
        if i >= k - 1:
            res.append(candidates[0][0])
    return res

if __name__ == '__main__':
    r = maxSlidingWindow2([1,3,-1,-3,5,3,6,7], 3)
    print(r)