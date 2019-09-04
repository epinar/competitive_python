

class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:

        resl = curr = ListNode(0)
        rem = 0
        while l1 or l2 or rem:
            if l1:
                rem += l1.val
                l1 = l1.next
            if l2:
                rem += l2.val
                l2 = l2.next
            rem, res = divmod(rem, 10)
            curr.next = curr = ListNode(res)
        return resl.next


if __name__ == '__main__':
    sol = Solution()
    list1 = ListNode(2)
    list1.next = ListNode(4)
    list1.next.next = ListNode(3)
    list2 = ListNode(5)
    list2.next = ListNode(6)
    list2.next.next = ListNode(4)
    l3 = ListNode(5)
    l4 = ListNode(5)
    #l4.next = ListNode(1)
    rel = sol.addTwoNumbers(l3, l4)
    while rel != None:
        print(rel.val)
        rel = rel.next

