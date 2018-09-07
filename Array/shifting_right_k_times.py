class Solution:
    def rotate(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: void Do not return anything, modify nums in-place instead.
        """

        #Input is a list of elements
        #output is the list shifted k times to the right
        #The shifting should be done in place
        #solution 1
        # Note when we right shift one step, what happens is that the last elemnt becomes the first,
        # and everything else is shifted to right, so the "insert(index, element)"" function will be useful
        if k > 0:
            l = len(nums)
            for j in range(k): #will shift one step at a time, k-times
                temp = nums[l-1] #need to save last elemnt before deleting it and right shifting one step
                nums.pop()    #deletes last elelement
                nums.insert(0, temp) #insert the deleted last element at the beginning of the list and shifting                                            #remaining element to the right
         