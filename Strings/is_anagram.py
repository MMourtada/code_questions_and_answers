class Solution:
    def isAnagram(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        #input is two string
        #output is True if the two strings are anagram of each other, and False otherwise
        result = False
        
        if set(s) == set(t):  #(if s and t have same set of characters, then investigate further)
            result = True
            for var in set(s):
                if s.count(var) != t.count(var):  #if one character that occured different times  
                    result = False         #in s and t then they're not anagram, break to save time
                    break
        return result
                