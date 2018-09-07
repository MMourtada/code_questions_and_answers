class Solution:
    def containsDuplicate(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """

        #Input: list of numbers
        #Output: True if there are is duplicates anf False if not 
        nums = sorted(nums)  #We sort the list to make it easier to find duplicates if any
        result = False  #initiate result to False:no duplicates, and change it to true if two consecutive elements
                        #in th esorted list are equal
        l = len(nums)
        for i in range(l-1):
            if nums[i] == nums[i+1]:
                result = True
                break   #to save time, since having one duplicate is enough to return True
            else:
                i += 1  # continue iterating 
        return result