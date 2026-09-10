# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        max_depth = 0

        def find_max_depth(node, curr_depth):
            if not node:
                return
            
            nonlocal max_depth
            max_depth = max(max_depth, curr_depth)
            
            find_max_depth(node.left, curr_depth + 1)
            find_max_depth(node.right, curr_depth + 1)
                

        find_max_depth(root, 1)
        return max_depth

        