# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def rotateRight(self, head, k):
        """
        :type head: ListNode
        :type k: int
        :rtype: ListNode
        """
        if not head: return None
        tail, ln = head, 1
        while tail.next: 
            tail = tail.next
            ln += 1
        k = k % ln
        
        tail.next = head
        for _ in range(ln - k):
            head = head.next
            tail = tail.next
        tail.next = None

        return head
