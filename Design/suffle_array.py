class Solution:
# define a class solution that shuffle, reset  an array
    def __init__(self, nums):      
        """
        :type nums: List[int]
        """
        self.items = nums
        

    def reset(self):
        """
        Resets the array to its original configuration and return it.
        :rtype: List[int]
        """
        return self.items 
        

    def shuffle(self):
        """
        Returns a random shuffling of the array.
        :rtype: List[int]
        """
        return random.sample(self.items, len(self.items))
        


# Your Solution object will be instantiated and called as such:
# obj = Solution(nums)
# param_1 = obj.reset()
# param_2 = obj.shuffle()