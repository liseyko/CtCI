# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None


class Solution:
    def deleteDuplicates(self, head: 'ListNode') -> 'ListNode':
        res = prev = ListNode(0)
        prev.next = cur = head
        while cur:
            if cur.next and cur.val == cur.next.val:
                while cur and cur.val == prev.next.val:
                    cur = cur.next
                prev.next = cur
            else:
                prev.next, prev, cur = cur, prev.next, cur.next
        return res.next
