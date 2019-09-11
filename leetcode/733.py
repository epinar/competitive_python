
import collections

def floodFill(image, sr, sc, newColor):
    oldColor = image[sr][sc]
    if oldColor == newColor:
        return image
    def flood_fill(row, col):
        if 0<=row<len(image) and 0<=col<len(image[0]):
            if image[row][col] == oldColor:
                image[row][col] = newColor
                flood_fill(row-1, col)
                flood_fill(row+1, col)
                flood_fill(row, col-1)
                flood_fill(row, col+1)
    flood_fill(sr, sc)
    return image


def floodFill2(image, sr, sc, newColor):
    oldColor = image[sr][sc]
    if oldColor == newColor:
        return image
    q = collections.deque([(sr, sc)])
    while q:
        i, j = q.popleft()
        image[i][j] = newColor
        for x, y in ((i-1, j), (i+1, j), (i, j-1), (i, j+1)):
            if 0<=x<len(image) and 0<=y<len(image[0]) and image[x][y] == oldColor:
                q.append((x, y))
    return image

if __name__ == '__main__':
    image = [[1, 1, 1], [1, 1, 0], [1, 0, 1]]
    sr = 1
    sc = 1
    newColor = 2
    #image = [[0, 0, 0], [0, 0, 0]]
    #sr , sc = 0, 0
    print(floodFill2(image, sr, sc, newColor))
