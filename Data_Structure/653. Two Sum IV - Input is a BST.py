# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def findTarget(self, root, k):
        if not root:
            return False
        stack = [root]
        seen = set()
        
        while stack:
            curr = stack.pop()
            if k-curr.val in seen:
                return True
            seen.add(curr.val)
            if curr.left:
                stack.append(curr.left)
            if curr.right:
                stack.append(curr.right)
        
        return False
      
        """
        :type root: TreeNode
        :type k: int
        :rtype: bool
        """
        """
        Time Complexity : O(n)
        Space Complexity : O(n)
        
