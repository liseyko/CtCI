# Definition for singly-linked list with a random pointer.
# class RandomListNode(object):
#     def __init__(self, x):
#         self.label = x
#         self.next = None
#         self.random = None


class Solution(object):
    def copyRandomList(self, head: 'Node') -> 'Node':
        nodes = {None: None}
        node = head
        while node:
            nodes[node.val] = Node(node.val, None, None)
            node = node.next
        node = head
        while node:
            nextNodeVal = node.next.val if node.next else None
            randomNodeVal = node.random.val if node.random else None
            nodes[node.val].next = nodes[nextNodeVal]
            nodes[node.val].random = nodes[randomNodeVal]
            node = node.next
        return nodes[head.val if head else None]

    def copyRandomList(self, head):
        """
        :type head: RandomListNode
        :rtype: RandomListNode
        """
        met = {None: None}

        def dfs(n):
            met[n] = RandomListNode(n.label)
            for c in (n.next, n.random):
                if c and c not in met:
                    dfs(c)
            met[n].next = met[n.next]
            met[n].random = met[n.random]
        if head:
            dfs(head)
            return met[head]

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
