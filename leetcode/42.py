

def trap(height):
    '''
    Keep the decreasing bar levels at a stack. When the bar levels start
    increasing, pop the smaller bars one by one, calculate the amount of water
    to be added in a horizontal manner. O(n) time, O(n) space.
    '''
    stack = []
    res = 0
    for i, h in enumerate(height):
        diff = 0
        while stack and stack[-1][0] < h:
            prev, _ = stack.pop()
            if stack:
                val, ind = stack[-1]
                diff += (min(h, val)-prev)*(i-ind-1)
        res += diff
        stack.append((h, i))
    return res

def trap2(height):
    '''
    Two pointer approach from front and end. Keep adding the water while
    the pointers meet.
    '''
    l, r = 0, len(height)-1
    l_max, r_max = 0, 0
    ans = 0
    while l < r:
        if height[l] < height[r]:
            if height[l] >= l_max:
                l_max = height[l]
            else:
                ans += l_max-height[l]
            l += 1
        else:
            if height[r] >= r_max:
                r_max = height[r]
            else:
                ans += r_max - height[r]
            r -= 1
    return ans


if __name__ == '__main__':

    arr = [0,1,0,2,1,0,1,3,2,1,2,1]
    #arr = [2, 1, 3, 1, 2]
    print(trap2(arr))