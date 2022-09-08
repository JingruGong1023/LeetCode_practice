'''
Input: target = 12, position = [10,8,0,5,3], speed = [2,4,1,1,3]
Output: 3
Explanation:
The cars starting at 10 (speed 2) and 8 (speed 4) become a fleet, meeting each other at 12.
The car starting at 0 does not catch up to any other car, so it is a fleet by itself.
The cars starting at 5 (speed 1) and 3 (speed 3) become a fleet, meeting each other at 6. The fleet moves at speed 1 until it reaches target.
Note that no other cars meet these fleets before the destination, so the answer is 3.
'''

'''
Understand the problem is the key
The problem is asking us to count the number of fleets created before or right at the time they arrive the target
Simply put, if a smaller position car, with a shorter time to get to the target comparing a larger position car, it means, they will meet before they arrive the target
We will use stack to store the position and speed, and another stack res to store the time needed to arrive target
if (target-position)/speed < res[-1], we pop one from res, the length of res at the end, is the number of fleet we want
'''

'''
create a stack storing pairs : position , speed 
res = []
reversely loop through the stack sorted by position -> because if we loop from the beginning, we might not know the car ahead's true speed
if length of res >=2(so that we can have a fleet ) and (target-position)/speed <= res[-2]
res.pop()
'''

class Solution(object):
    def carFleet(self, target, position, speed):
        res = []
        stack = [[p,s] for p, s in zip(position, speed)]
        
        for p,s in sorted(stack)[::-1]:
            time = (target-p)/float(s)
            res.append(time)
            if len(res)>=2 and res[-2]>=res[-1]:
                res.pop()
        return len(res)
        
        """
       Time Complexity : O(n)
       Space Complexity : O(n)
        """
        
