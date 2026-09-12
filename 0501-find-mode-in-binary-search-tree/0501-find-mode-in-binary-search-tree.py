# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def findMode(self, root: Optional[TreeNode]) -> List[int]:
        self.res = []
        self.max_count = 0
        self.prev_val = None
        self.curr_count = 0

        def dfs(node):
            if not node:
                return
            
            dfs(node.left)

            if node.val == self.prev_val:
                self.curr_count += 1
            else:
                self.curr_count = 1
                self.prev_val = node.val
            
            if self.curr_count == self.max_count:
                self.res.append(node.val)
            elif self.curr_count > self.max_count:
                self.max_count = self.curr_count
                self.res = [node.val]
            
            dfs(node.right)
        dfs(root)
        return self.res