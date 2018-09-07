class MinStack:
# Design a stack that supports push, pop, top, and retrieving the minimum element in constant time.

#push(x) -- Push element x onto stack.
#pop() -- Removes the element on top of the stack.
#top() -- Get the top element.
#getMin() -- Retrieve the minimum element in the stack.
    def __init__(self):
        """
        initialize your data structure here.
        """
        self.items = []
        

    def push(self, x):
        """
        :type x: int
        :rtype: void
        """
        self.items.append(x)

    def pop(self):
        """
        :rtype: void
        """
        return self.items.pop()
        

    def top(self):
        """
        :rtype: int
        """
        return self.items[-1]
        

    def getMin(self):
        """
        :rtype: int
        """
        return min(self.items)
        


# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(x)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()