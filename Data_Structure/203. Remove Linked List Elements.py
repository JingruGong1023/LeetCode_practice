# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def removeElements(self, head, val):
        
        prev = ListNode(0)
        prev.next = head
        prevv = prev
        curr = head
        
        while curr:
            if curr.val == val:
                prev.next = curr.next
            else:
                prev = curr
            curr = curr.next
        return prevv.next
        
        """
        :type head: ListNode
        :type val: int
        :rtype: ListNode
        """
