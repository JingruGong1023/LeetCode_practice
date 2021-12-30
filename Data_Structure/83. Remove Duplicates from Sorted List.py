# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def deleteDuplicates(self, head):
        if head is None or head.next is None:
            return head
        else:
            visited = []
            curr = head
            while curr.next:
                visited.append(curr.val)
                if curr.next.val in visited:
                    curr.next = curr.next.next
                else:
                    curr = curr.next
            return head 
        """
        :type head: ListNode
        :rtype: ListNode
        """
        
