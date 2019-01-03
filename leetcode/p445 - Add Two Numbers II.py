# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def addTwoNumbers(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        s = t = 0
        if not l1 and not l2:
            return None
        while l1:
            s = s*10 + l1.val
            l1 = l1.next
        while l2:
            t = t*10 + l2.val
            l2 = l2.next
        s += t
        if not s:
            return ListNode(0)
        head = tail = None
        while s:
            s, digit = divmod(s, 10)
            head = ListNode(digit)
            head.next , tail = tail, head
        return head

    def addTwoNumbers(self, l1, l2):
        stack1, stack2, carry = [], [], 0
        while l1:
            stack1.append(l1.val)
            l1 = l1.next
        while l2:
            stack2.append(l2.val)
            l2 = l2.next
        res = None
        while stack1 or stack2 or carry:
            if stack1:
                carry += stack1.pop()
            if stack2:
                carry += stack2.pop()
            carry, val = divmod(carry, 10)
            head = ListNode(val)
            head.next, res = res, head
        return res

class Solution:
    def addTwoNumbers(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        cur1, cur2 = l1, l2
        length1 = length2 = 0

        while cur1:
            length1 += 1
            cur1 = cur1.next
        while cur2:
            length2 += 1
            cur2 = cur2.next

        dummy = ListNode(None)
        cur1, cur2 = l1, l2        
        while cur1 or cur2:
            if length1 > length2:
                node = ListNode(cur1.val)
                node.next = dummy.next
                dummy.next = node
                cur1 = cur1.next
                length1 -= 1
            elif length2 > length1:
                node = ListNode(cur2.val)
                node.next = dummy.next
                dummy.next = node
                cur2 = cur2.next
                length2 -= 1
            else:
                node = ListNode(cur1.val + cur2.val)
                node.next = dummy.next
                dummy.next = node
                cur1 = cur1.next
                cur2 = cur2.next
                length1 -= 1
                length2 -= 1

        res = ListNode(None)
        carry = 0
        cur = dummy.next
        while cur:
            sum = carry + cur.val
            node = ListNode(sum % 10)
            node.next = res.next
            res.next = node
            carry = sum // 10
            cur = cur.next

        if carry:
            node = ListNode(1)
            node.next = res.next
            res.next = node
        return res.next
