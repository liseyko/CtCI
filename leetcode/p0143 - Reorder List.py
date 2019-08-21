# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def reorderList(self, head):
        """
        :type head: ListNode
        :rtype: void Do not return anything, modify head in-place instead.
        """
        if not head: return
        
        p1 = p2 = head
        while p1 and p1.next:
            p1 = p1.next.next
            p2 = p2.next
            
        p1 = p2.next
        p2.next = None
        while p1:
            p3 = p1.next
            p1.next = p2
            p2 = p1
            p1 = p3
        p1 = head

        while p1.next and p2.next:
            p3 = p1.next
            p1.next = p2
            p1 = p3
            p3 = p2.next
            p2.next = p1
            p2 = p3
