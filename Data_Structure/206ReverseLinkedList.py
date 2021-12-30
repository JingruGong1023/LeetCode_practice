# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

#Iterative
class Solution(object):
    def reverseList(self, head):
        if head is None or head.next is None:
            return head
        curr = head
        prev = None
        
        while curr:
            nxt = curr.next
            curr.next = prev
            prev = curr
            curr=nxt
        return prev
        """
        :type head: ListNode
        :rtype: ListNode
        """
        """
        Time Complexity: O(n)
        Space Complexity : O(1)
        """
     
#Recursiveclass Solution(object):

    def reverseList(self, head):
        if head is None or head.next is None:
            return head
        
        p = self.reverseList(head.next)
        head.next.next = head
        head.next = None
        return p
        """
        Time Complexity: O(n)
        Space Complexity : O(n)
        """
