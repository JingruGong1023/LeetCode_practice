# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def lowestCommonAncestor(self, root, p, q):
        parent = root.val
        p_val = p.val
        q_val = q.val
        
        if p_val < parent and q_val <parent:
            return self.lowestCommonAncestor(root.left,p,q)
        elif p_val > parent and q_val > parent:
            return self.lowestCommonAncestor(root.right,p,q)
        else:
            return root
        """
        :type root: TreeNode
        :type p: TreeNode
        :type q: TreeNode
        :rtype: TreeNode
        """
        """
        Time Complexity: O(n)
        Space Complexity : O(n)
        
        Iterative:
        """
        class Solution(object):
    def lowestCommonAncestor(self, root, p, q):
       
        p_val = p.val
        q_val = q.val
        
        stack = [root]
        while stack:
            node = stack.pop()
            parent = node.val
            if p_val < parent and q_val <parent:
                node = node.left
                stack.append(node)
            elif p_val > parent and q_val > parent:
                node = node.right
                stack.append(node)
            else:
                return node
            
