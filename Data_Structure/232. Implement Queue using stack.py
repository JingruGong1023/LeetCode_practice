class MyQueue(object):

    def __init__(self):
        self._items = []
        

    def push(self, x):
        self._items.append(x)
        """
        :type x: int
        :rtype: None
        """
        

    def pop(self):
        if self.empty is True:
            return 
        else:
            return self._items.pop(0)
        """
        :rtype: int
        """
        

    def peek(self):
        if self.empty is True:
            return 
        else:
            return self._items[0]
        """
        :rtype: int
        """
        

    def empty(self):
        if len(self._items)==0:
            return True
        else:
            return False
        """
        :rtype: bool
        """
        


# Your MyQueue object will be instantiated and called as such:
# obj = MyQueue()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.peek()
# param_4 = obj.empty()
