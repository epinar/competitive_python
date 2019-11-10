

class ListNode(object):
    def __init__(self, x):
         self.val = x
         self.next = None

def getIntersectionNode(headA, headB):
    stA, stB = [], []

    if headA is None or headB is None:
        return None

    while headA:
        stA.insert(0, headA)
        headA = headA.next

    while headB:
        stB.insert(0, headB)
        headB = headB.next

    ct = 0
    while ct<len(stA) and ct<len(stB) and stA[ct] == stB[ct]:
        ct += 1

    if ct == 0:
        return None

    return stA[ct-1].val



if __name__ == '__main__':

    headA = ListNode(4)
    headA.next = ListNode(1)
    intersection = ListNode(8)
    headA.next.next = intersection
    headA.next.next.next = ListNode(4)
    headA.next.next.next.next = ListNode(5)

    headB = ListNode(5)
    headB.next = ListNode(0)
    headB.next.next = ListNode(1)
    headB.next.next.next = intersection

    print(getIntersectionNode(headA, headB))

    headC = ListNode(0)
    headC.next = ListNode(9)
    headC.next.next = ListNode(1)
    intersection = ListNode(2)

    headC.next.next.next = intersection
    headC.next.next.next.next = ListNode(4)

    headD = ListNode(3)
    headD.next = intersection

    #print(getIntersectionNode(headC, headD))

    headE = ListNode(1)
    headF = headE
    print(getIntersectionNode(headE, headF))


