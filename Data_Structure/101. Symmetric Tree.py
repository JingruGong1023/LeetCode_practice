# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def isSymmetric(self, root):
        if not root:
            return False
        stack = []
        stack=[(root.left,root.right)]
        while stack:
            left,right = stack.pop()
            if left is None and right is None:
                continue
            if left is None or right is None:
                return False
            if left.val ==right.val:
                stack.append((left.left,right.right))
                stack.append((right.left,left.right))
            else:
                return False
        return True
        """
        :type root: TreeNode
        :rtype: bool
        """
        """
        Time Complexity: O(n)
        Space Complexity : O(n)
        
