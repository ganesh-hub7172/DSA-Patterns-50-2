class Solution:
    def evaluateTree(self, root):
        if not root.left and not root.right:
            return root.val == 1

        left = self.evaluateTree(root.left)
        right = self.evaluateTree(root.right)

        if root.val == 2:
            return left or right
        else:
            return left and right
