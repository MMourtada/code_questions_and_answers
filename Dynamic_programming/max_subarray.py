
#In this problem, we have a list of integers,
# we need to find the max sum a sublist of it could have

##This solution works but it doesn't tell what is the max subarray
class Solution:
    def maxSubArray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        n = len(nums)
        for i in range(1, n):
            if nums[i-1] > 0:
                nums[i] += nums[i-1]    #Aggregated sum, when previous is positive, add it to the new
        return max(nums)


#divide and conquer sol that passed all test cases including last one. 
#It has the potential of finding the max subarray as well, and not just the sum
class Solution:
    def maxSubArray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """

       n = len(nums)
        if n == 1:
            return nums[0]
        #compute the maxsubarray on first half and second half of list
        left_max = self.maxSubArray(nums[:n//2])
        right_max = self.maxSubArray(nums[n//2:])  
        
        right_sum = nums[n//2]
        left_sum = nums[n//2-1]
        
        #Now compute the max we can get out of a middle subarray, and not an edge subarray
        temp = 0
        for i in range(n//2):
            temp = temp + nums[n//2-1-i]   
            if temp > left_sum:
                left_sum = temp
       
                
        temp = 0
        for i in range(n//2, n):
            temp = temp + nums[i]
            if temp > right_sum:
                right_sum = temp
                

        return max(left_max, right_max, right_sum, left_sum, right_sum+left_sum)

      #right_sum+left_sum because we can take a middle subarray containing both element from right
      #and elements from left



###correct divide and conquer, passed all test cases except for last one: time limit exceeded
class Solution:
    def maxSubArray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        n = len(nums)
        max_sum = sum(nums)
        max_sub = nums[:]
      
            
        if n == 1:
            return nums[0]
            self.maxSubArray = nums
        elif n == 2:
            if min(nums) < 0:
                return max(nums)
                self.maxSubArray = [max(nums)]
            elif max(nums) <= 0:
                return max(nums)
                self.maxSubArray =[max(nums)]
            
            elif min(nums) >= 0:
                return sum(nums)
                self.maxSubArray =  nums
        elif n >= 3:
            temp1 = nums[n//2+1:]
            sum1 = sum(temp1)
            max_sub1 = []
            while temp1:
                if sum(temp1) > sum1:
                    sum1 = sum(temp1)
                    max_sub1 = temp1
                temp1.pop()
            temp2 = nums[:n//2+1]
            sum2 = sum(temp2)
            max_sub2 = []
            while temp2:
                if sum(temp2) > sum2:
                    sum2 = sum(temp2)
                    max_sub2 = temp2
                del temp2[0]
            
            return max(self.maxSubArray(nums[0:n//2]),self.maxSubArray(nums[n//2+1:n]), sum(nums), sum1+sum2,sum1, sum2 )

   