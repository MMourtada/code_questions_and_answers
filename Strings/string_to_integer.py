
class Solution:
    def myAtoi(self, str):
        """
        :type str: str
        :rtype: int
        """  


"""
input : string with posssible whitspaces
output: integer.
The function first discards as many whitespace characters as necessary until 
the first non-whitespace character is found. Then, starting from this character, 
takes an optional initial minus sign followed by as many numerical digits as possible,
and interprets them as a numerical value.
If no valid conversion could be performed, a zero value is returned.
Assume we are dealing with an environment which could only store integers within the 32-bit signed 
integer range: [−231,  231 − 1]. If the numerical value is out of the range of representable values,
INT_MAX (231 − 1) or INT_MIN (−231) is returned.
"""

        ans = ""   #initialize answer to empty
      
        if str == "":    #if input is empty, return 0
            return 0
        if str[0] ==" ":    #Keep discarding first whitespace
            return self.myAtoi(str[1:])
        if str[0] == "-":    #when there is minus sign, put it in front of answer
            ans = ans + "-" 
            str = str[1:]
        elif str[0] == "+":   #if plus sign, discard it
            str = str[1:]
        
        for char in str:
            if char not in ["0", "1","2", "3", "4", "5", "6", "7", "8", "9"]:
                break   #if character not among these 10 difits, break
            else:
                ans = ans + char  #consider the character otherwise
                
        if  ans == "" or ans == "-":  
            return 0
   
        elif int(ans) <-2**31:
            return -2**31
        elif int(ans) > 2**31-1:
            return 2**31-1
    
        else:
            return int(ans)
            