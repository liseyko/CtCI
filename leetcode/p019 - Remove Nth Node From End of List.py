# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def removeNthFromEnd(self, head, n):
        """
        :type head: ListNode
        :type n: int
        :rtype: ListNode
        """
        b, f = head, head
        for _ in range(n):
            f = f.next

        if not f:
            return head.next

        while f.next:
            f = f.next
            b = b.next

        b.next = b.next.next

        return head
