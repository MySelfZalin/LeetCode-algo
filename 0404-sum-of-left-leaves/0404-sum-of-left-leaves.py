# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sumOfLeftLeaves(self, root: Optional[TreeNode]) -> int:
        def left_subtree_val(node, isLeft):
            if not node:
                return 0
            
            if (not node.left and not node.right) and isLeft:
                return node.val

            return left_subtree_val(node.left, True) + left_subtree_val(node.right, False)
    
        return left_subtree_val(root, False)
        