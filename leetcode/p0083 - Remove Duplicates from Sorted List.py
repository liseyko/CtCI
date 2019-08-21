# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def deleteDuplicates(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        r = head
        while head:
            i = head.next
            while i and head.val == i.val:
                i = i.next
            head.next = i
            head = i
        return r