from heapq import *

class MedianFinder_lame:

    def __init__(self):

        self.nums = []
        self.n = 0

    def addNum(self, num: int) -> None:
        self.n += 1
        def get_pos(num, nums):
            l, r = 0, len(nums)-1
            while l<=r:
                mid = (l+r)//2
                if nums[mid]<num:
                    l = mid+1
                else:
                    r = mid-1
            return l
            
        p = get_pos(num, self.nums)
        print("insert: ", p)
        self.nums.insert(p, num)
        

    def findMedian(self) -> float:
        if self.n == 0:
            return None
        elif self.n == 1:
            return self.nums[0]
        elif self.n % 2 != 0:
            return self.nums[self.n//2]
        else:
            return (self.nums[self.n//2]+self.nums[self.n//2-1])/2


class MedianFinder_cool:

    def __init__(self):

        self.hi = []
        self.lo = []

    def addNum(self, num: int) -> None:
        if len(self.hi) == len(self.lo):
            heappush(self.hi, -heappushpop(self.lo, -num))
        else:
            heappush(self.lo, -heappushpop(self.hi, num))

    def findMedian(self) -> float:
        if len(self.lo) == len(self.hi):
            return (self.hi[0] - self.lo[0])/2
        else:
            return self.hi[0]
        

def testcase1():
    obj = MedianFinder_cool()
    obj.addNum(-1)
    print("median, ", obj.findMedian())
    obj.addNum(-2)
    print(obj.findMedian())
    obj.addNum(-3)
    print(obj.findMedian())
    obj.addNum(-4)
    print(obj.findMedian())
    obj.addNum(-5)
    print(obj.findMedian())

def testcase2():
    obj = MedianFinder_cool()
    obj.addNum(1)
    print("median, ", obj.findMedian())
    obj.addNum(2)
    print(obj.findMedian())
    obj.addNum(3)
    print(obj.findMedian())
    obj.addNum(4)
    print(obj.findMedian())
    obj.addNum(5)
    print(obj.findMedian())

if __name__ == '__main__':
    testcase2()