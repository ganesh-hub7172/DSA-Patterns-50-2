class Solution:
    def getAllElements(self, root1, root2):
        
        def inorder(root, arr):
            if not root:
                return
            inorder(root.left, arr)
            arr.append(root.val)
            inorder(root.right, arr)
        
        list1 = []
        list2 = []
        
        inorder(root1, list1)
        inorder(root2, list2)
        
        # Merge two sorted lists
        i = j = 0
        merged = []
        
        while i < len(list1) and j < len(list2):
            if list1[i] < list2[j]:
                merged.append(list1[i])
                i += 1
            else:
                merged.append(list2[j])
                j += 1
        
        # Add remaining elements
        merged.extend(list1[i:])
        merged.extend(list2[j:])
        
        return merged
