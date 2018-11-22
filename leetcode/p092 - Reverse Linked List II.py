class Solution:
    def reverseBetween(self, head, m, n):
        """
        :type head: ListNode
        :type m: int
        :type n: int
        :rtype: ListNode
        """
        if m == 1:
            l, c, r = None, head, head.next
        else:
            l = head
            for i in range(m-2):
                l = l.next
            c, r = l.next, l.next.next
        
        for i in range(n-m):
            t = c
            c = r
            r = c.next
            c.next = t
            
        if not l:
            head.next = r
            head = c
        else:
            l.next.next = r
            l.next = c
        
        return head