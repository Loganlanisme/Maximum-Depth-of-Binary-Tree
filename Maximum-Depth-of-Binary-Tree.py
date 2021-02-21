class Solution:
    def maxDepth(self, root: TreeNode) -> int:
        if not root:
            return 0
        result = []
        queue = []
        queue.append(root)
        depth = 0

        while queue:
            nodes = []
            for i in range(len(queue)):
                node = queue.pop(0)
                nodes.append(node.val)

                if node.left:
                    queue.append(node.left)

                if node.right:
                    queue.append(node.right)

            depth += 1

        return depth


class Solution:
    def maxDepth(self, root: TreeNode) -> int:
        if not root:
            return 0
        else:
            return max(self.maxDepth(root.left),self.maxDepth(root.right))+1