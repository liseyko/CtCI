# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None


class Solution:
    def partition(self, head: 'ListNode', x: 'int') -> 'ListNode':
        cur = head
        head1 = tail1 = ListNode(0)
        head2 = tail2 = ListNode(0)
        while cur:
            print(cur.val)
            if cur.val < x:
                tail1.next = cur
                tail1 = tail1.next
            else:
                tail2.next = cur
                tail2 = tail2.next
            cur = cur.next
        tail1.next, tail2.next = head2.next, None
        return head1.next
