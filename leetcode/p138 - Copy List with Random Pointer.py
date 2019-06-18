"""
# Definition for a Node.
class Node:
    def __init__(self, val, next, random):
        self.val = val
        self.next = next
        self.random = random
"""


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

    def copyRandomList(self, head: 'Node') -> 'Node':
        nodes = {None: None}

        def dfs(node):
            nodes[node] = Node(node.val, None, None)
            for nextNode in (node.next, node.random):
                if nextNode and nextNode not in nodes:
                    dfs(nextNode)
            nodes[node].next = nodes[node.next]
            nodes[node].random = nodes[node.random]

        if head:
            dfs(head)
        return nodes[head]

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
