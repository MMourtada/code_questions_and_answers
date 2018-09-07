class Solution:
    def moveZeroes(self, nums):
        """
        :type nums: List[int]
        :rtype: void Do not return anything, modify nums in-place instead.
        """
        #Input is a list with possibly zero entries
        #should change the list in place so that zeros arte moved to the end, 
        #while reserving the order of other entries
        l = len(nums)
        i = 0
        temp_l = l #temporary length of sublist with non-zeros 
        while i < temp_l: #when all zeros are pushed to end, no need to keep iterating
            if nums[i] == 0:
                del nums[i]
                nums.append(0)
                temp_l = temp_l -1
            else:
                i += 1
            