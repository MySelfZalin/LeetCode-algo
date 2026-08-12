from collections import deque

class Solution:
    def isSymmetric(self, root: Optional[TreeNode]) -> bool:
        queue = deque()
        queue.append((root.left, root.right))
        
        while queue:
            first, second = queue.popleft()

            if not first and not second:
                continue

            if not first or not second or first.val != second.val:
                return False

            queue.append((first.left, second.right))
            queue.append((first.right, second.left))
        return True    
                
        
            
        