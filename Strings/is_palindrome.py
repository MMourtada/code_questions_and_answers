class Solution:
    def isPalindrome(self, s):
        """
        :type s: str
        :rtype: bool
        """
        """
        Given a string, determine if it is a palindrome(same string after reversal),
        considering only alphanumeric characters and ignoring cases.
        Note: For the purpose of this problem, we define empty string as valid palindrome.
        """
        #Input is a string
        #Output is True if the string is Palindrome, and False otherwise.
        chars = "abcdefghijklmnopqrstuvwxyz0123456789"
        s = s.lower()
        for var in s:
            if var not in chars:
                s = s.replace(var, "")
        retrun s == s[::-1]

