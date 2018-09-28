class Solution:
    def shortestPalindrome(self, s):
        """
        :type s: str
        :rtype: str
        """
        """
        Given a string s, you are allowed to convert it to a palindrome by adding characters in front of it. 
        Find and return the shortest palindrome you can find by performing this transformation.
        """ 
        i = len(s)
        while  i > 0:
            if s[:i] == s[:i][::-1]:     #scanning for longest palindrome contained in s starting from beginning
                break                     #if found, break
                                            
                                      #else, consider the substring without last element
            else:                            
                i = i-1
        return  s[i:][::-1] + s          #Once found the longest substring that is a palindrom, add to it the reverse 
                                         #of the remaining ending substring