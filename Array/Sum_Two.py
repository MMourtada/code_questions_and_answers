class Solution:
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
      #Input is a list of integers with a target an integer n
      #output is the unique couple of entries in the list that sum up to the target n
      #we can assume the couple sol is unique
      # the same index shouldn't be used more than once
        l = len(nums)
    
        if nums.count(target//2) == 2:    # If half the target is in the list twise then that's the answer
            s = nums.index(target//2)
            t = nums.index(target//2, s+1)
            return [s, t]
        else:
            temp = sorted([w for w in nums if w < target/2])   #Split the nums list into elements less than 
                                            #half target and another larger than half target,
                #the answer will consist of an elemnt in first sublist and another in second sublist
            tempr = sorted([w for w in nums if w > target/2], reverse = True)
            for i in range(len(temp)):
                for j in range(len(tempr)):
                    if temp[i] + tempr[j] == target:
                        s = nums.index(temp[i])
                        t = nums.index(tempr[j])
                        return sorted([s,t])
                    else: 
                        j += 1 
                i+= 1