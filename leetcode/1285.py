

def findNumbers(nums):
    res = 0

    def isEven(n):
        d = 0
        while n / 10 != 0:
            print(n)
            d += 1
            n = int(n / 10)
        return d % 2 == 0

    for n in nums:
        if isEven(n):
            res += 1

    return res

nums = [1]

output = findNumbers(nums)

print(output)