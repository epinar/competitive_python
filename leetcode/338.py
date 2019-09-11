
def countBits(num):

    res = [0]
    if num > 0:
        while len(res) < num+1:
            res.extend([x+1 for x in res])
    return res[0:num+1]

if __name__ == '__main__':

    print(countBits(5))
