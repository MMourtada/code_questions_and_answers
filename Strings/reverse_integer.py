class Solution:
    def reverse(self, x):
        """
        :type x: int
        :rtype: int
        """
        """
        Assume we are dealing with an environment which could only store integers 
        within the 32-bit signed integer range: [−231,  231 − 1]. For the purpose of this problem,
        assume that your function returns 0 when the reversed integer overflows.
        """
        # Input is an integer
        # Output is the same digits of the input integer put in a reversed order
        if x in range(-9, 9):  #No need to reverse if it is one digit integer
            return x 
        
        elif x > 0:
            x = int(str(x)[::-1])   #It is easier to reverse a tring instead
            
       
        elif x <0:
            x = -int(str(-x)[::-1])
            
        if -2**31 <= x <= 2**31-1:     #If x overflows after reversal, return zero
            return x
        else:
            return 0