class Solution:
    def singleNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        # Input is a non-empty list of integers where every element is repeated twice except for one
        #Output is the non-repeated element
        l = len(nums)
        if l == 1:      #if the list consists of one element then return that element
            result = nums[0]
        else:
            nums = sorted(nums)  #we sort the list to make it easier to spot the non repeated element
            if nums[0] < nums[1]:
                result = nums[0]
            else:
                for i in range(1, l-3):
                    if nums[i] < nums[i+1] < nums[i+2]:
                        result = nums[i+1]
                        break
                    else:
                        i += 1
                        if i == l-3:
                            if nums[l-3]<nums[l-2]<nums[l-1]:
                                result = nums[l-2]
                            else:
                                result = nums[l-1]
                        
                
        return result