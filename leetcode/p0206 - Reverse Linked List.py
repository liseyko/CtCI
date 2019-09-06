# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None


class Solution:
    def reverseList(self, head: ListNode) -> ListNode:
        if head and head.next:
            revBody = self.reverseList(head.next)
            head.next.next, head.next = head, None
            head = revBody
        return head

    def reverseList(self, head: ListNode) -> ListNode:
        prev, curr = None, head
        while curr:
            next = curr.next
            curr.next = prev
            prev, curr = curr, next
        return prev
