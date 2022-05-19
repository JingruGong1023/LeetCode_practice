'''
Input: head = [3,2,0,-4], pos = 1
Output: true
Explanation: There is a cycle in the linked list, where the tail connects to the 1st node (0-indexed).
'''

'''
let p1 = head, p2 = head.next, two pointers, one move a step forward, one moves two steps forward
if a cycled linkedlist, two pointers will meet eventually, otherwise one of them or one's next will meet None eventually
when we do the while loop, except check if two pointer are None, we need to check if p2.next is None, to avoid error
'''

'''
思路:
edge case: 
if not head -> return False

two pointers : slow = head, fast = head.next. 
slow moves one step, fast moves two steps
while slow and fast not None -> means, if a cycled linkedlist, they will never meet None
and fast.next is not None, to avoid error, because we need to move two steps for fast, None does not have next
once fast = slow: return True
else: fast = fast.next.next, slow = slow.next
if ever break the loop, means there is None at the end, so not a cycled LinkedList -> return False
'''

# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def hasCycle(self, head):
        if not head:
            return False
        fast = head.next
        slow = head
        
        while (fast is not None and slow is not None and fast.next is not None):
          if fast == slow:
            return True
          else:
            fast = fast.next.next
            slow = slow.next
       return False

'''
Time Complexity : O(n)
Space Complexity : O(1)
'''









