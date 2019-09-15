
from collections import Counter, defaultdict

def topKFrequent(nums, k):
    c = Counter(nums).most_common(k)
    res = [k for k, v in c]
    return res

def topKFrequent2(nums, k):
    '''
    This is a fantastic solution!
    '''
    frq = defaultdict(list)
    for key, cnt in Counter(nums).items():
        frq[cnt].append(key)

    res = []
    for times in reversed(range(len(nums) + 1)):
        res.extend(frq[times])
        if len(res) >= k: return res[:k]

    return res[:k]

if __name__ == '__main__':
    res = topKFrequent2([1,1,1,2,2,3], 2)
    #res = topKFrequent([1, 2, 2], 2)
    #res = topKFrequent([3,2,3,1,2,4,5,5,6,7,7,8,2,3,1,1,1,10,11,5,6,2,4,7,8,5,6], 10)
    print(res)