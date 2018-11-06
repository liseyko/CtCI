# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution(object):
    def detectCycle(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        if not head: return None
        slow = fast = head
        
        while fast.next and fast.next.next:
            slow, fast = slow.next, fast.next.next
            if slow == fast:
                fast = head
                while slow != fast:
                    slow, fast = slow.next, fast.next
                return slow

        return None



if __name__ == '__main__':
    n = ListNode(0)
    n1 = n.next = ListNode(1)
    n2 = n.next.next = ListNode(2)
    n3 = n.next.next.next = ListNode(3)
    n3.next = n3


    s = Solution()
    print(s.detectCycle(n).val)