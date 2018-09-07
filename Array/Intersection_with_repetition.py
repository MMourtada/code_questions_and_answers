class Solution:
    def intersect(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: List[int]
        """
        #Input is two lists that could be very large
        #output is their intersection with possible repetition
        #Try your best to be meory efficient
        
        inter = [] #We initiate the intersection to be empty list
        nums1 = sorted(nums1) # Sort bcz it's easier to track repeated elements in sorted lists
                              #Sort in place to save memory
        nums2 = sorted(nums2)
        l = min(len(nums1), len(nums2))  #Work with the list of min length to save time and memory
        if l == len(nums1):   #If the smaller list is nums1
            while l >0:
                if nums1[-1] in nums2:     #start with the end of list
                    inter.append(nums1[-1])
                    nums2.remove(nums1[-1])   #remove the intersection so that it's not inserted extra times
                nums1.pop()
                l = l - 1
        else:
             while l >0:
                if nums2[-1] in nums1:  #if nums2 is the smallest list, do the same code above but roles switched
                    inter.append(nums2[-1])
                    nums1.remove(nums2[-1])
                nums2.pop()
                l = l - 1
                
            
        return inter