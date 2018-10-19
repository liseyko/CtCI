import heapq
#from Queue import PriorityQueue
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
        """
        q, h = len(lists), []
        for i in range(q):
            if lists[i]:
                heapq.heappush(h, (lists[i].val, i, lists[i]))
        
        rhead = rtail = ListNode(0)
        
        while h:
            i, n = heapq.heappop(h)[1:]
            rtail.next = n
            rtail = rtail.next
            if n.next:
                heapq.heappush(h, (n.next.val, i, n.next))
                
        return rhead.next
        #Time complexity : O(Nlogk)
        #Space complexity : O(n+k)

# TODO: Merge with Divide And Conquer
"""
Pair up k lists and merge each pair.
After the first pairing, k lists are merged into k/2 lists with average 2N/k length, then k/4, k/8 and so on.
Repeat this procedure until we get the final sorted linked list.
Time complexity : O(Nlogk)
Space complexity : O(1)
"""