# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None


class Solution:
    def swapPairs(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        # 1->2->3->4 => 2->1->4->3
        # h->1->2<-t
        if not head or not head.next:
            return head
        h, t = head, head.next
        head, p = head.next, ListNode(-1)
        while h and t:
            h.next = t.next
            t.next = h
            p.next = t
            p = h
            h = h.next
            if h:
                t = h.next

        return head

    def swapPairs(self, head: ListNode) -> ListNode:
        """ Recursive """
        if not head or not head.next:
            return head
        node3 = head.next.next
        head.next.next = head
        head = head.next
        head.next.next = self.swapPairs(node3)
        return head
