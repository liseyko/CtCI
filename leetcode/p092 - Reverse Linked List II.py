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


    def reverseBetween(self, head: ListNode, m: int, n: int) -> ListNode:
        prv = None
        cur = head
        nxt = head.next if head else None
        for _ in range(m-1):
            prv, cur, nxt = cur, nxt, nxt.next

        subhead, subtail = cur, prv

        for _ in range(m, n+1):
            cur.next = prv
            prv = cur
            cur = nxt
            nxt = nxt.next if nxt else None

        if subtail:
            subtail.next = prv
        subhead.next = cur

        return prv if m==1 else head
