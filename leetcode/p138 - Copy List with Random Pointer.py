# Definition for singly-linked list with a random pointer.
# class RandomListNode(object):
#     def __init__(self, x):
#         self.label = x
#         self.next = None
#         self.random = None
class Solution(object):
    def copyRandomList(self, head):
        """
        :type head: RandomListNode
        :rtype: RandomListNode
        """
        if not head: return None
        vis = {head.label: RandomListNode(head.label)}
        n = head

        while n:
            if n.random:
                if n.random.label not in vis:
                    vis[n.random.label] = RandomListNode(n.random.label)
                vis[n.label].random = vis[n.random.label]
            if n.next:
                if n.next.label not in vis:
                    vis[n.next.label] = RandomListNode(n.next.label)
                vis[n.label].next = vis[n.next.label]

            n = n.next
            
        return vis[head.label]

    def copyRandomList(self, head):
        if not head:
            return 
        # copy nodes
        cur = head
        while cur:
            nxt = cur.next
            cur.next = RandomListNode(cur.label)
            cur.next.next = nxt
            cur = nxt
        # copy random pointers
        cur = head
        while cur:
            if cur.random:
                cur.next.random = cur.random.next
            cur = cur.next.next
        # separate two parts
        second = cur = head.next
        while cur.next:
            head.next = cur.next
            head = head.next
            cur.next = head.next
            cur = cur.next
        head.next = None
        return second