class Solution(object):
    def isHappy(self, n):
        """
        :type n: int
        :rtype: bool
        """
        #a new function returns the next number(sum of squares of each digit)
        def get_next(number):
            total_sum = 0
            while number>0:
                number, digit = divmod(number,10) #return quotient and remainder
                total_sum +=digit **2
            return total_sum
            
        slow = n 
        fast = get_next(n) #so fast is one step ahead 
        
        #if fast ==1: happy number
        #if slow == fast : enter a loop
        while fast!=1 and slow != fast: 
            slow = get_next(slow)
            fast = get_next(get_next(fast))#fast jump two steps every time
        return fast ==1
        
        """
        Time Complexity : O(logn)
        Space Complexity : O(1)
        """
