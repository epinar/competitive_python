
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


def detectCycle(head):

    '''
    Floyd's cycle detection algorithm.
    Let k be distance turtle moved. Hence, rabbit moves 2k.
    Let s be the distance from head to start of cycle.
    Let m be the distance from start of the cycle to the first meeting point of
        rabbit and turtle.
    Let r be length of cycle.
    k = s + m
    2k = s + m + r
    Hence, we have s = r - m.
    The first loop finds m.
    Second loop finds s. (curr moves s many times, f moves r - m times, we return when it is equal, s=r-m).
    '''

    try:
        fast = head.next
        slow = head
        while fast is not slow:
            slow = slow.next
            fast = fast.next.next
    except:
        return None

    slow = slow.next
    while head is not slow:
        head = head.next
        slow = slow.next

    return head


if __name__ == '__main__':

    head = ListNode(3)
    cycle = ListNode(2)
    head.next = cycle
    cycle.next = ListNode(0)
    cycle.next.next = ListNode(-4)
    cycle.next.next.next = cycle


    head = ListNode(1)
    cycle = ListNode(2)
    head.next = cycle
    cycle.next = head


    #head = ListNode(1)

    print(detectCycle(head).val)