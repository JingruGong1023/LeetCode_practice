# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def inorderTraversal(self, root):
        stack = []
        result = []
        while stack or root:
            while root:
                stack.append(root) #this will add the root into the stack
                root = root.left
            root = stack.pop() #will pop the left most root
            result.append(root.val) 
            root = root.right #after go over the left, go to the right
        return result
        
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        
