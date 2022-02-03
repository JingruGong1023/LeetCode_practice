# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def getIntersectionNode(self, headA, headB):
        nodesB = set()
        while headB is not None:
            nodesB.add(headB)
            headB = headB.next
        
        while headA is not None:
            if headA in nodesB:
                return headA
            headA = headA.next
        return None
        """
        :type head1, head1: ListNode
        :rtype: ListNode
        Time complexity : O(N+M)
        Space complexity : O(M)
        """
        
