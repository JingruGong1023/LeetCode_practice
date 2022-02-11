# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def addTwoNumbers(self, l1, l2):
        
        dummy = cur = ListNode(0)
        carry = 0
        
        while carry or l1 or l2:
            if l1:
                carry += l1.val
                l1=l1.next
            if l2:
                carry+=l2.val
                l2= l2.next
            cur.next=ListNode(carry%10)
            cur = cur.next
            carry = carry//10
        return dummy.next
        
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        Time Complexity : O(max(m,n))
        Space Complexity : O(max(m,n))
        """
        
