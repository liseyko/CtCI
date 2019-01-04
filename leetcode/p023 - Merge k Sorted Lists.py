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


"""
TODO: Merge with Divide And Conquer
Pair up k lists and merge each pair.
After the first pairing, k lists are merged into k/2 lists with
average 2N/k length, then k/4, k/8 and so on.
Repeat this procedure until we get the final sorted linked list.
Time complexity : O(Nlogk)
Space complexity : O(1)
"""
