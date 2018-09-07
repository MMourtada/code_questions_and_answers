class Solution:
  
    def removeDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: int
       """
        #need two iterator: i that will iterate thru the indices of the list without duplicates, and j that will 
        # iterate thru the original one. Every time we find a new entry we put it next:
        if(len(nums)<2):
            return len(nums)
        else: 
            i = 0
            for j in range(1, len(nums)):
                if nums[j] != nums[i]:
                    i=i+1
                    nums[i] = nums[j]
            return i+1  #because the last index i in the for loop is for the last element
                        # and the lenth of a list is equal to the last index +1 in Python