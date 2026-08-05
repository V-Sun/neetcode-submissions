# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def lowestCommonAncestor(self, root: TreeNode, p: TreeNode, q: TreeNode) -> TreeNode:
        curr = root

        if not curr or not p or not q:
            return None
        if max(p.val, q.val) >= curr.val and min(p.val, q.val) <= curr.val:
            return curr
        if max(p.val, q.val) > curr.val and min(p.val, q.val) > curr.val:
            curr = curr.right
        else:
            curr = curr.left
        
        return self.lowestCommonAncestor(curr, p, q)
        
