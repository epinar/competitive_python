
from typing import List


def maxArea(height: List[int]) -> int:

    L , R = 0, len(height)-1
    res = 0
    while L < R:
        curr_area = min(height[L], height[R]) * (R-L)
        res = max(res, curr_area)

        if height[L] > height[R]:
            R -= 1
        else:
            L += 1
    return res


if __name__ == '__main__':
    a = maxArea([2, 3, 10, 5, 7, 8, 9])
    print(a)