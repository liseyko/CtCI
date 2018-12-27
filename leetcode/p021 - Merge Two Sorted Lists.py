class Solution(object):
    def mergeTwoLists(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        if not l1:
            return l2
        if not l2:
            return l1

        if l2.val < l1.val:
            l1, l2 = l2, l1
        head = l1

        while l2:
            while l1.next and l1.next.val < l2.val:
                l1 = l1.next
            l1.next, l2 = l2, l1.next
            l1 = l1.next
        return head

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
