
import heapq

class ListNode:

    def __init__(self, x):
        self.val = x
        self.next = None

def mergeKLists(lists):

    '''
    At each step, find the next minimum element from the lists, append to result.
    '''

    h = ListNode(0)
    next_node = h

    if len(lists) == 0:
        return None

    for i in range(len(lists) - 1, -1, -1):
        if lists[i] == None:
            lists.pop(i)

    while lists:
        min_num = float('inf')
        min_i = -1
        for n, l in enumerate(lists):
            if l.val < min_num:
                min_num = l.val
                min_i = n
        if lists[min_i].next != None:
            lists[min_i] = lists[min_i].next
        else:
            lists.pop(min_i)
        next_node.next = ListNode(min_num)
        next_node = next_node.next

    return h.next


def mergeKLists2(lists):
    '''
    Optimized version of previous solution. Use a priority queue to keep the initial elements. At each step, when the node is removed, add node.next to the priority queue.
    '''

    h = ListNode(0)
    next_node = h

    if len(lists) == 0:
        return None

    heap = []

    for n, l in enumerate(lists):
        if l != None:
            heapq.heappush(heap, (l.val, n))

    while heap:
        min_num, min_i = heapq.heappop(heap)
        next_node.next = ListNode(min_num)
        next_node = next_node.next
        lists[min_i] = lists[min_i].next
        if lists[min_i] != None:
            heapq.heappush(heap, (lists[min_i].val, min_i))

    return h.next


def mergeKLists3(lists):
    '''
    Totally different approach than others. Merge the lists two by two until we
     end up with only one list.
    '''

    h = ListNode(0)
    next_node = h

    def mergeLists(l1, l2):
        h = nextnode = ListNode(0)
        while l1 or l2:
            if l1 and l2:
                if l1.val < l2.val:
                    nextnode.next = ListNode(l1.val)
                    l1 = l1.next
                else:
                    nextnode.next = ListNode(l2.val)
                    l2 = l2.next
            elif l1:
                nextnode.next = ListNode(l1.val)
                l1 = l1.next
            else:
                nextnode.next = ListNode(l2.val)
                l2 = l2.next
            nextnode = nextnode.next
        return h.next


    while len(lists)!=1:
        for i in range(len(lists)-1, 0, -2):
            lists[i] = mergeLists(lists[i], lists[i-1])
            lists.pop(i-1)
            print(i, " : ", len(lists))

    return lists[0]



if __name__ == '__main__':

    l1 = ListNode(1)
    l1.next = ListNode(4)
    l1.next.next = ListNode(5)

    l2 = ListNode(1)
    l2.next = ListNode(3)
    l2.next.next = ListNode(4)

    l3 = ListNode(2)
    l3.next = ListNode(6)

    ans = mergeKLists3([l1, l2, l3])

    while ans:
        print(ans.val)
        ans = ans.next