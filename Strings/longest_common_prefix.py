class Solution:
    def longestCommonPrefix(self, strs):
        """
        :type strs: List[str]
        :rtype: str
         Write a function to find the longest common prefix string amongst an array of strings.
         If there is no common prefix, return an empty string "".
        :type strs: List[str]
        :rtype: str
        """
        
        if strs == []:
            return ""
        
        ans = ""
        i = 0  #will run thru indices of first string in the list
           
      
        L = len(strs)
        for char in strs[0]:   #
            j = 1
      
            while j < L and i < len(strs[j]):  #check for each string of length larger 
                                            #than the running index of char if it contains  char              if strs[j][i]!= char:
                    break                   #if not break return ans so far
                    return ans
                else:
                    j += 1                 #otherwise, check for next string in the list
            if j == L:
                ans = ans + char           #If we make it all the way to the end, then char 
                                            #is a common character, so add it to the answer 
                i += 1
            else:                 #else, stop break, no more "for" looping
                break
            
        return ans