


def reconstructQueue(people):

    people = sorted(people, key = lambda x: (-x[0], x[1]))
    res = []
    for p in people:
        res.insert(p[1], p)
    return res


if __name__ == '__main__':
    res = reconstructQueue([[7,0], [4,4], [7,1], [5,0], [6,1], [5,2]])
    print(res)