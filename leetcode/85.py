

def maximalRectangle(matrix):

    '''
    It is a similar problem with largest rectangle in histogram. Here,
    instead of one level, we have #row levels to check. Keep the consecutive
    number of vertical blocks in height.
    '''

    if not matrix or not matrix[0]:
        return 0

    R, C = len(matrix), len(matrix[0])
    res = 0
    height = [0] * (C+1)
    for r in range(R):
        for c in range(C):
            if matrix[r][c] == '1':
                height[c] = height[c] + 1
            else:
                height[c] = 0
        stack = [-1]
        for c in range(C+1):
            while height[c] < height[stack[-1]]:
                h = height[stack.pop()]
                w = c - 1 - stack[-1]
                res = max(res, h*w)
            stack.append(c)
    return res

def maximalRectangle2(matrix):
    '''
    DP solution, at each row level, keep the left and right boundaries, also the height.
    Calculate the area based on the (right-left)*height.
    '''
    if not matrix or not matrix[0]:
        return 0

    R, C = len(matrix), len(matrix[0])
    res = 0
    left = [0] * C
    right = [C] * C
    height = [0] * C

    for i in range(R):
        curr_left, curr_right = 0, C
        for j in range(C):
            if matrix[i][j] == '1':
                height[j] += 1
            else:
                height[j] = 0

        for j in range(C):
            if matrix[i][j] == '1':
                left[j] = max(left[j], curr_left)
            else:
                left[j] = 0
                curr_left = j+1

        for j in range(C-1, -1, -1):
            if matrix[i][j] == '1':
                right[j] = min(right[j], curr_right)
            else:
                right[j] = C
                curr_right = j

        for j in range(C):
            res = max(res, (right[j]-left[j])*height[j])
    return res


print(maximalRectangle2([
  ["1","0","1","0","0"],
  ["1","0","1","1","1"],
  ["1","1","1","1","1"],
  ["1","0","0","1","0"]
]))