class Solution(object):
    def addDigits(self, num):
        def get_next(n):
            result = 0
            while n >0:
                n, digit = divmod(n,10)
                result += digit
            return result
            
        value = get_next(num)
        while len(str(value))>1:
            value = get_next(value)
        return value
            
        """
        :type num: int
        :rtype: int
        """
