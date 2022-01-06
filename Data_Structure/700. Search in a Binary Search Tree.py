# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
#Recursive
class Solution(object):
    def searchBST(self, root, val):
        if not root or root.val == val:
            return root
        
        if root.val<val:
            return self.searchBST(root.right,val)
        elif root.val>val:
            return self.searchBST(root.left,val)
        
       
        """
        :type root: TreeNode
        :type val: int
        :rtype: TreeNode
        """
 
#Iterative

class Solution(object):
    def searchBST(self, root, val):
        if not root or root.val == val:
            return root
        
        while root and root.val != val:
            if root.val<val:
                root = root.right
            else:
                root= root.left
        return root
        
        """
        :type root: TreeNode
        :type val: int
        :rtype: TreeNode
        """
        
        
        
