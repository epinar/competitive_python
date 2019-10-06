
def searchMatrix(matrix, target):


    d, u = 0, len(matrix)-1
    while d <= u:
        mid = (u+d)//2
        if matrix[mid][0] <= target:
            d = mid+1
        else:
            u = mid-1
    row = (u+d)//2

    l, r = 0, len(matrix[0])-1
    while l <= r:
        mid = (l+r)//2
        if matrix[row][mid] <= target:
            l = mid+1
        else:
            r = mid-1
    col = (r+l)//2

    return matrix[row][col] == target


def searchMatrix2(matrix, target):
    if not matrix or target is None:
        return False

    rows, cols = len(matrix), len(matrix[0])
    low, high = 0, rows * cols - 1

    while low <= high:
        mid = (low + high) // 2
        num = matrix[mid // cols][mid % cols]

        if num == target:
            return True
        elif num < target:
            low = mid + 1
        else:
            high = mid - 1

    return False

if __name__ == '__main__':

    matrix = [
        [1, 3, 5, 7],
        [10, 11, 16, 20],
        [23, 30, 34, 50]
    ]

    print(searchMatrix2(matrix, 30))