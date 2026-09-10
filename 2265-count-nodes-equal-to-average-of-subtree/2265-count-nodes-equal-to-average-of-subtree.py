# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:

    def averageOfSubtree(self, root: TreeNode) -> int:
        def help_func(node: TreeNode) -> tuple: #сумма, коллво элементов
            if node is None:
                return (0, 0)
            
            left_subtree = help_func(node.left)
            right_subtree = help_func(node.right)
            values_subtree = (left_subtree[0] + right_subtree[0] + node.val, left_subtree[1] + right_subtree[1] + 1)
            if node.val == values_subtree[0] // values_subtree[1]:
                nonlocal count
                count += 1
            return values_subtree
        
        count = 0
        help_func(root)
        return count


        
            



