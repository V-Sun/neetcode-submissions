# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        
        def goodNodeCheck(node, maxVal):
            if node is None:
                return 0
            
            res = 0
            if node.val >= maxVal:
                res = 1
                maxVal = node.val
            
            res += goodNodeCheck(node.left, maxVal)
            res += goodNodeCheck(node.right, maxVal)

            return res

        return goodNodeCheck(root, root.val)