# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def addTwoNumbers(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        r = ListNode(0)
        result = r
        s, t = 0, 0
        while l1 or l2:
            if r.next:
                r = r.next
            if l1:
                s += l1.val
                l1 = l1.next
            if l2:
                s += l2.val
                l2 = l2.next
            t = s // 10
            s = s % 10
            r.val = s
            s = t
            r.next = ListNode(0)

        if s>0:
            r.next.val = s
        else:
            r.next = None

        return result