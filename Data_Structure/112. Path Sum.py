# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
#Recursive
class Solution(object):
    def hasPathSum(self, root, targetSum):
        if not root:
            return False
        
        targetSum -= root.val
        if not root.left and not root.right:
            return targetSum==0
        return self.hasPathSum(root.left, targetSum) or self.hasPathSum(root.right, targetSum)
        """
        :type root: TreeNode
        :type targetSum: int
        :rtype: bool
        """
        
 #Iterative
class Solution(object):
    def hasPathSum(self, root, targetSum):
        if not root:
            return False
        
        stack = [(root, targetSum - root.val)]
        
        while stack:
            node, sum = stack.pop()
            if not node.left and not node.right and sum ==0:
                return True
            if node.right:
                stack.append((node.right, sum-node.right.val))
            if node.left:
                stack.append((node.left, sum - node.left.val))
        return False
        
        
        """
        Time Complexity: O(n)
        Space Complexity: O(logn)
