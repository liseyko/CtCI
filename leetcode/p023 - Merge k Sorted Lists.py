import heapq
# Definition for singly-linked list.
"""
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None
"""


class Solution(object):
    def mergeKLists(self, lists):
        """
        :type lists: List[ListNode]
        :rtype: ListNode
        Time/space complexity : O(Nlogk) / O(n+k)
        """
        res = cur = ListNode(-1)
        h = []
        for i, l in enumerate(lists):
            if l:
                heapq.heappush(h, (l.val, i, l))
        while h:
            i, n = heapq.heappop(h)[1:]
            cur.next = n
            cur = cur.next
            if n.next:
                heapq.heappush(h, (n.next.val, i, n.next))
        return res.next

    def merge2Lists(self, l1, l2):
        res = cur = ListNode(-1)
        while l1 and l2:
            if l1.val <= l2.val:
                cur.next = l1
                l1 = l1.next
            else:
                cur.next = l2
                l2 = l2.next
            cur = cur.next
        cur.next = l1 or l2
        return res.next

    def mergeKLists(self, lists):
        """
        Merge with Divide And Conquer
        Pair up k lists and merge each pair.
        After the first pairing, k lists are merged into k/2 lists with
        average 2N/k length, then k/4, k/8 and so on.
        Repeat this procedure until we get the final sorted linked list.
        Time complexity : O(Nlogk)
        Space complexity : O(1)
        """
        ll = len(lists)
        while ll > 1:
            lists = [self.merge2Lists(pair[0], pair[1]) for pair in
                     itertools.zip_longest(lists[:ll//2], lists[ll//2:])]
            ll = len(lists)
        if not lists:
            return lists
        return lists[0]
