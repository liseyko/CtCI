# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def removeElements(self, head, val):
        while head and head.val == val:
            head = head.next
        if not head:
            return None
        n = head
        while c.next:
            if n.next.val != val:
                n = n.next
            else:
                n.next = n.next.next
        return head
