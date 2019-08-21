# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None


class Solution:
    def reverseList(self, head: ListNode) -> ListNode:
        if not head:
            return head
        cur, nxt = head, head.next
        prv = cur.next = None
        while nxt:
            prv, cur, nxt = cur, nxt, nxt.next
            cur.next = prv
        return cur

    def reverseList(self, head):
        if head and head.next:
            reversed_body = self.reverseList(head.next)
            head.next.next, head.next = head, None
            head = reversed_body
        return head

    def reverseList(self, head):
        prev, curr = None, head
        while curr:
            next = curr.next
            curr.next = prev
            prev, curr = curr, next
        return prev
