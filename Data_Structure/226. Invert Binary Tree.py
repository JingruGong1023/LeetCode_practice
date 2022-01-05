# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

#Recursive
class Solution(object):
    def invertTree(self, root):
        if not root:
            return 
        
        right = self.invertTree(root.right)
        left = self.invertTree(root.left)
        root.left = right
        root.right = left
        return root
                
        """
        :type root: TreeNode
        :rtype: TreeNode
        """
       
#iterative
class Solution(object):
    def invertTree(self, root):
        if not root:
            return 
        
        stack = [root]
        
        while stack:
            node = stack.pop()
            if node:
                node.left, node.right = node.right, node.left
                stack.extend([node.left, node.right])
        
        return root
