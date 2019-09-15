

def subsets(nums):
    n = len(nums)
    res = []

    def map_binary(j):
        curr = []
        k = n-1
        while j != 0:
            if j%2 == 1:
                curr.append(nums[k])
            k -= 1
            j  = int(j/2)
        return curr

    for i in range(2**n):
        res_new = map_binary(i)
        res.append(res_new)

    return res

def subsets2(nums):
    result = [[]]
    for num in nums:
        result += [i + [num] for i in result]
    return result

if __name__ == '__main__':
    print(subsets([1, 2, 3]))
    print(subsets([1, 2]))
    print(subsets([1]))
    print(subsets2([1, 3, 1]))