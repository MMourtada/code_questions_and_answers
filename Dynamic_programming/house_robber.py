class Solution:
    def rob(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
      # input is a list of positive numbers representing money to rob from a sequence of houses
      #output is the max amount of money u can rob, given theat u cannot rob two adjacent houses

        n = len(nums)
        if n == 0:               #Will use divide and conquer
            return 0
        elif n == 1:
            return max(nums) 
            #The optimal path could either contain the middle point nums[n//2] or not

     
        right_path = self.rob(nums[n//2+1:])
        left_path = self.rob(nums[:n//2])
        path_no_middle = right_path+left_path #if middle house is not robbed
        right_path = self.rob(nums[n//2+2:])
        left_path = self.rob(nums[:n//2-1])
        path_with_middle = right_path+left_path + nums[n//2]  #if middle house is robbed
        return max(path_no_middle, path_with_middle)

