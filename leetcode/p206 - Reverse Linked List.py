# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def reverseList(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        if not head or not head.next: return head
        
        p, c, n = None, head, head.next
        while n:
            c.next = p
            p = c
            c = n
            n = n.next
        c.next = p
        return c

    def reverseList(self, head):
        if not head or not head.next: return head
        p = self.reverseList(head.next)
        head.next.next = head
        head.next = None
        return p
    
    def reverseList(self, head):
        prev, curr = None, head
    
        while curr:
            next = curr.next
            curr.next = prev
            prev = curr
            curr = next

        return prev