"""
# Definition for a Node.
class Node(object):
    def __init__(self, val, prev, next, child):
        self.val = val
        self.prev = prev
        self.next = next
        self.child = child
"""
class Solution(object):
    def flatten(self, head):
        """
        :type head: Node
        :rtype: Node
        """
        curr, next = head, None
        while curr:
            if curr.child:
                next = curr.next
                curr.child.prev = curr
                curr.next = self.flatten(curr.child)
                curr.child = None
            prev, curr = curr, curr.next
        if next:
            prev.next = next
            next.prev = prev
            self.flatten(next)
        
        return head
    
    #def flatten(self, head):    
        #TODO: iterative with stack