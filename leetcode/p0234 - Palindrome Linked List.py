class Solution:
    def isPalindrome(self, head):
        """
        :type head: ListNode
        :rtype: bool
        """
        fast = slow = head
        stack = []
        while fast and fast.next:
            stack.append(slow.val)
            slow = slow.next
            fast = fast.next.next
        if fast:
            slow = slow.next
        while slow:
            if stack.pop() != slow.val:
                return False
            slow = slow.next
        return True

    def isPalindrome(self, head):
        fast = slow = head
        prev = None
        while fast and fast.next:
            fast = fast.next.next
            next, slow.next, prev = slow.next, prev, slow
            slow = next

        if fast:
            slow = slow.next

        while slow:
            if prev.val != slow.val:
                return False
            prev, slow = prev.next, slow.next

        return True
