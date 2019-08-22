# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

    def addTwoNumbers(self, l1, l2):
        res = cur = ListNode(0)
        carry = 0
        while l1 or l2 or carry:
            if l1:
                carry += l1.val
                l1 = l1.next
            if l2:
                carry += l2.val
                l2 = l2.next
            cur.next = ListNode(carry%10)
            cur = cur.next
            carry //= 10
        return res.next

    def addTwoNumbers(self, *lls):
        overflow = 0
        res = cur = ListNode(0)
        lls = list(lls)
        while any(lls) or overflow:
            for i, l in enumerate(lls):
                if l:
                    overflow += l.val
                    lls[i] = lls[i].next
                    
            cur.next = ListNode(overflow % 10)
            cur = cur.next
            overflow //= 10

        return res.next