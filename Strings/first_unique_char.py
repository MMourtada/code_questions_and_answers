
class Solution:
    def firstUniqChar(self, s):
        """
        :type s: str
        :rtype: int
        """
        #Input is a string
        #output is the index of first unique character in the string, -1 if none
        chars = set(s)
        result = -1
        unique = [s.index(var) for var in chars if s.count(var) == 1]
        if unique:
            result = min(unique)
        return result
