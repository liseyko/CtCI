# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def getIntersectionNode(self, headA, headB):
        """
        :type head1, head1: ListNode
        :rtype: ListNode
        """
        slow, fast = headA, headB # blind assumption
        if not slow or not fast:
            return None
        
        while slow.next and fast.next and slow != fast:
            slow, fast  = slow.next, fast.next

        if not slow.next: 
            slow, fast = fast, slow
            headA, headB = headB, headA
        diff = 0
        while slow != fast and slow.next:
            slow, diff = slow.next, diff + 1

        if slow != fast: 
            return None

        slow, fast = headA, headB
        for _ in range(diff):
            slow = slow.next
        
        while slow != fast:
            slow, fast  = slow.next, fast.next

        return slow
    
    def getIntersectionNode(self, headA, headB):
        a, b = headA, headB        
        if not a or not b: return None
        
        for _ in range(3):
            while a and b and a != b:
                a, b  = a.next, b.next 
            if not a: a = headB
            if not b: b = headA

        if a != b: return None
        return a