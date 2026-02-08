class Solution:
    def allPossibleFBT(self, n):
        memo = {}

        def dfs(nodes):
            if nodes in memo:
                return memo[nodes]

            res = []
            if nodes == 1:
                res.append(TreeNode(0))
            elif nodes % 2 == 1:
                for left_nodes in range(1, nodes, 2):
                    right_nodes = nodes - 1 - left_nodes
                    for left in dfs(left_nodes):
                        for right in dfs(right_nodes):
                            root = TreeNode(0)
                            root.left = left
                            root.right = right
                            res.append(root)

            memo[nodes] = res
            return res

        return dfs(n)
