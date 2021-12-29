# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def hasCycle(self, head):
        if head is None:
            return False
        fast = head
        slow = head
        while(fast != None and fast.next != None ):
            fast = fast.next.next
            slow = slow.next
            if fast == slow:
                return True
    
        
        return False

    
    
        """
        :type head: ListNode
        :rtype: bool
        """
        """
        Floyd's Cycle Finding Algorithm
        If there is no cycle in the list, the fast pointer will eventually reach the end and we can return false in this case.
        Time Complexity: O(n)
        Space Complexity : O(1)
