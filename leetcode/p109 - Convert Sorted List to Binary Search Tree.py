# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def sortedListToBST(self, head):
        """
        :type head: ListNode
        :rtype: TreeNode
        """
        if not head: return None
        if not head.next: return TreeNode(head.val)
        if not head.next.next: 
                h = TreeNode(head.val)
                h.right = TreeNode(head.next.val)
                return h
        
        slow, fast = head, head
        while fast.next and fast.next.next:
            slow_p = slow
            slow, fast = slow.next, fast.next.next

        tHead = TreeNode(slow.val)
        slow_p.next = None
        tHead.left = self.sortedListToBST(head)
        tHead.right = self.sortedListToBST(slow.next)
        return tHead