from collections import deque

class Solution:
    def findLexSmallestString(self, s, a, b):
        visited = set()
        queue = deque([s])
        visited.add(s)
        
        smallest = s
        
        while queue:
            cur = queue.popleft()
            
            if cur < smallest:
                smallest = cur
            
            # Operation 1: Add 'a' to odd indices
            temp = list(cur)
            for i in range(1, len(temp), 2):
                temp[i] = str((int(temp[i]) + a) % 10)
            add_op = "".join(temp)
            
            if add_op not in visited:
                visited.add(add_op)
                queue.append(add_op)
            
            # Operation 2: Rotate right by b
            rotate_op = cur[-b:] + cur[:-b]
            
            if rotate_op not in visited:
                visited.add(rotate_op)
                queue.append(rotate_op)
        
        return smallest
