class Solution:
    def plusOne(self, digits):
        """
        :type digits: List[int]
        :rtype: List[int]
        """
        # Input is a list of integers represent the digits of a number x.
        #Output is the number x plus one, written as a list of digits
        l = len(digits)
        if digits[-1] < 9:
            digits[-1] += 1 
            return digits    #in this case it's easy to add one, just add it to the ones digit
        else:
            digits[-1] = 0  
            i = l- 2      #move on to next digit from right
            while i>=0:
                if digits[i] < 9:
                    digits[i] += 1
                    break
                else:
                    digits[i] = 0
                    i = i-1
            if i == -1:    # if all digits are 9 then this is where we get, in this case an additional digit
                                          #will be inserted first place from left
                digits.insert(0, 1)
                    
            return digits