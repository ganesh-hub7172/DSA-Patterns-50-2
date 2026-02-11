class Solution:
    def postorder(self, root):
        result = []
        
        def dfs(node):
            if not node:
                return
            
            for child in node.children:
                dfs(child)
            
            result.append(node.val)
        
        dfs(root)
        return result
