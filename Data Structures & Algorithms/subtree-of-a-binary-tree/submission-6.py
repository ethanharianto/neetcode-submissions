# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:   
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        def sameTree(one, two):
            if not one and not two:
                return True
            if one and two and one.val == two.val:
                return sameTree(one.left, two.left) and sameTree(one.right, two.right)
            return False
        if not subRoot:
            return True
        if not root:
            return False 
        if sameTree(root, subRoot):
            return True
        return self.isSubtree(root.left, subRoot) or self.isSubtree(root.right, subRoot)