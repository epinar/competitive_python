

def countSmaller(nums):

    ord = []
    ans = []

    for i in range(len(nums)-1, -1, -1):

        num = nums[i]
        l, r = 0, len(ord)
        while l<r:
            mid = (l+r)//2
            if ord[mid]<num:
                l=mid+1
            else:
                r=mid

        ord.insert(l, num) # l is the place of num to put on ordered list
        ans.insert(0, l) # l is also number of smaller numbers seen so far

    return ans




nums = [5,2,6,1]
nums = [5, 4, 3, 2, 1, 5]
print(countSmaller(nums))

