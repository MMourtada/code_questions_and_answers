class Solution:
    def climbStairs(self, n):
        """
        :type n: int
        :rtype: int
        """
        #Input is the number of steps in a stair
        #Output is the number of distinct ways you can climb the stairs 
        #given that you can at each time euther climb one step or two steps 
        if n <= 3:
            return n   #Just try it out
        else:
            s = [1,2]     #Notice this follows Fibonacci sequence, 
            #since the number of different ways to climb n steps is: 
            #you can climb n-1 steps then take one more step ...>this is numbe rof ways to climb (n-1)
            #or you can climb n-2 steps then take two steps ...> this is numbe rof ways to climb (n-2)
            for i in range(3, n):
                s.append(s[-1] + s[-2])
            return s[-1] + s[-2]

            