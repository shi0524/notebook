# Definition for singly-linked list.

class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


def mergeTwoLists(l1, l2):
    """
    :type l1: ListNode
    :type l2: ListNode
    :rtype: ListNode
    """
    if not l1 or not l2:
        return l1 if l1 else l2
    head = l1 if l1.val <= l2.val else l2
    cur1 = head.next
    cur2 = l2 if head==l1 else l1
    pre = head

    while (cur1 != None and cur2!=None):
        if cur1.val <= cur2.val:
            pre.next = cur1
            cur1 = cur1.next
        else:
            pre.next = cur2
            cur2 = cur2.next
        pre = pre.next
    pre.next = cur1 if cur1 else cur2

    return head

def mergeTwoLists2(l1, l2):
    """
    :type l1: ListNode
    :type l2: ListNode
    :rtype: ListNode
    """
    if not l1 or not l2:
        return l1 if l1 else l2
    head = l1 if l1.val <= l2.val else l2
    cur1 = head.next
    cur2 = l2 if head==l1 else l1
    pre = head

    while (cur1 and cur2):
        if cur1.val <= cur2.val:
            pre.next = cur1
            cur1 = cur1.next
        else:
            pre.next = cur2
            cur2 = cur2.next
        pre = pre.next
    pre.next = cur1 if cur1 else cur2
    return head

def print_link(head):
    n = 10
    while head and n:
        print head.val,
        head = head.next
        n -= 1
    print

if __name__ == "__main__":
    """
    l1 = [1,2,4], l2 = [1,3,4]
    """
    n1 = ListNode(1)
    n2 = ListNode(2)
    n3 = ListNode(3)
    l1 = n1
    l1.next = n2
    l1.next.next = n3

    m1 = ListNode(10)
    m2 = ListNode(20)
    m3 = ListNode(30)
    l2 = m1
    l2.next = m2
    l2.next.next = m3


    head = mergeTwoLists2(l1, l2)
    print_link(head)
