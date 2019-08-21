# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None


class Solution(object):
    def getIntersectionNode(self, headA, headB):
        if not (headA and headB):
            return None
        pa, pb = headA, headB
        for _ in range(3):
            while pa and pb:
                if pa == pb:
                    return pa
                pa, pb = pa.next, pb.next
            pa = headB if not pa else pa
            pb = headA if not pb else pb

    def getIntersectionNode(self, headA, headB):
        """
        :type head1, head1: ListNode
        :rtype: ListNode
        """
        offset = 0
        for _ in range(2):
            curA, curB = headA, headB
            while offset:
                curA = curA.next
                offset -= 1
            while curA and curB:
                if curA == curB:
                    return curA
                curA = curA.next
                curB = curB.next
            cur = curA or curB
            if curB:
                headA, headB = headB, headA
            while cur:
                cur = cur.next
                offset += 1
