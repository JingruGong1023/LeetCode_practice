# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

#Iterative
class Solution(object):
    
    def maxDepth(self, root):
        if root is None:
            return 0
        if not root.right and not root.left:
            return 1
        level = 0
        stack = []
        if root is not None:
            stack.append((1,root))
        while stack:
            current,root = stack.pop()
            
            if root is not None:
                level = max(current,level)#incase that only one side has children
                stack.append((current+1, root.left))
                stack.append((current+1, root.right))
        
        return level
        """
        :type root: TreeNode
        :rtype: int
        """
        """
        Time complexity: O(n)
        Space Complexity : O(logn)
        
# Recursive
class Solution(object): 
    def maxDepth(self, root):
        if not root:
            return 0
        left = 1+self.maxDepth(root.left)
        right = 1+self.maxDepth(root.right)
        return max(left, right)
        """
        :type root: TreeNode
        :rtype: int
        """
        
        
        
