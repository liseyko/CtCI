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
        if not headA or not headB:
            return None
        ptr1, ptr2 = headA, headB
        onePass1, onePass2 = 1, 1
        while ptr1 != ptr2:
            ptr1, ptr2 = ptr1.next, ptr2.next
            if not ptr1 and onePass1:
                ptr1, onePass1 = headB, onePass1-1
            if not ptr2 and onePass2:
                ptr2, onePass2 = headA, onePass2-1
        return ptr1 if ptr1 == ptr2 else None

    def getIntersectionNode(self, headA, headB):
        if not headA or not headB:
            return None
        pa, pb = headA, headB
        for _ in range(3):
            while pa and pb and pa != pb:
                pa, pb = pa.next, pb.next
            if not pa:
                pa = headB
            if not pb:
                pb = headA
        return pa if pa == pb else None
