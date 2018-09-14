#This solution reverse it in place
class Solution:
    def reverseString(self, s):
        """
        :type s: str
        :rtype: str
        """
        s = s[::-1]
        return s



#This solution create a new reversed list
class Solution:
    def reverseString(self, s):
        """
        :type s: str
        :rtype: str
        """
        n = len(s)
        rev = ""
        for i in range(n):
            rev = rev + s[n-1-i]
            
        return rev


#This solution reverse it in place but takes a bit longer 
class Solution:
    def reverseString(self, s):
        """
        :type s: str
        :rtype: str
        """
  
        n = len(s)
        
        for i in range(n):
            s = s + s[n-1-i]

        return s[n:]