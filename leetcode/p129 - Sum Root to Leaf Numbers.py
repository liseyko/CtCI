    def sumNumbers(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        self.result = 0
        
        def dfs(node = root, num = 0):
            num = num * 10 + node.val            
            if not node.left and not node.right:
                self.result += num
                return
            for child in node.left, node.right:
                if child:
                    dfs(child, num)
        if root:
            dfs()
        return self.result

    def sumNumbers(self, root):
        if not root: return 0
        result = 0
        stack = [(root, root.val)]
        while stack:
            node, val = stack.pop()
            if not node.left and not node.right:
                result += val
            else:
                for child in node.left, node.right:
                    if child:
                        stack.append((child, val * 10 + child.val))

        return result