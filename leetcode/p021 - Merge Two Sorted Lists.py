# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None


class Solution:

    def mergeTwoLists(self, l1, l2):
        res = cur = ListNode(-1)
        while l1 and l2:
            if l1.val < l2.val:
                cur.next = l1
                l1 = l1.next
            else:
                cur.next = l2
                l2 = l2.next
            cur = cur.next
        cur.next = l1 or l2
        return res.next

    def mergeTwoLists(self, l1, l2):
        if not (l1 and l2):
            return l1 or l2
        if l1.val < l2.val:
            l1.next = self.mergeTwoLists(l1.next, l2)
            return l1
        else:
            l2.next = self.mergeTwoLists(l2.next, l1)
            return l2

    def mergeTwoLists(self, l1, l2):
        if not (l1 and l2):
            return l1 or l2

        if l2.val < l1.val:
            l1, l2 = l2, l1
        head = l1

        while l2:
            while l1.next and l1.next.val < l2.val:
                l1 = l1.next
            l1.next, l2 = l2, l1.next
            l1 = l1.next

        return head
