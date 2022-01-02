# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def preorderTraversal(self, root):
        if root is None:
            return []
        stack = [root]
        curr = []
        while stack:
            root = stack.pop()
            if root is not None:
                curr.append(root.val)
                #Since stack is FIFO, we go over right first here
                if root.right is not None:
                    stack.append(root.right)
                if root.left is not None:
                    stack.append(root.left)
                
        return curr
                
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        """
        Using Stack: FIFO
        Time Complexity : O(n)
        Space Complexity : O(n)
