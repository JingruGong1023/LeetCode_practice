# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

#Iterative
class Solution(object):
    def insertIntoBST(self, root, val):
        if not root:
            return TreeNode(val) #create a new tree with val as node
        
        node = root
        while node:
            if val >node.val:
                if not node.right:
                    node.right = TreeNode(val)
                    return root
                else:
                    node = node.right
            else:
                if not node.left:
                    node.left = TreeNode(val)
                    return root
                else:
                    node = node.left
      
        
        """
        :type root: TreeNode
        :type val: int
        :rtype: TreeNode
        """
        
        #Recursive
        class Solution(object):
    def insertIntoBST(self, root, val):
        if not root:
            return TreeNode(val) #create a new tree with val as node
        
        if root.val>val:
            root.left = self.insertIntoBST(root.left,val)
        else:
            root.right = self.insertIntoBST(root.right,val)
        
        
        return root
        
