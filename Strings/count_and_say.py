class Solution:
    def countAndSay(self, n):
        """
        :type n: int
        :rtype: str
        The count-and-say sequence is the sequence of integers with the first five terms
        as follows:1, 11, 21, 1211, 111221


         1 is read off as "one 1" or 11.
         11 is read off as "two 1s" or 21.
         21 is read off as "one 2, then one 1" or 1211.

         Given an integer n where 1 ≤ n ≤ 30, generate the nth term of the count-and-say sequence.

         Note: Each term of the sequence of integers will be represented as a string.

        """


        if n == 1:
            return str(1)
        if n== 2:
            return str(11)
        if n == 3:
            return str(21)
        if n == 4:
            return str(1211)
        if n == 5:
            return str(111221)
        if n > 5:
            ans = ""
            prev = self.countAndSay(n-1)
            l = len(prev)
            i = 0
            while i < l-1:
                counter = 1
                while i < l-1 and prev[i] == prev[i+1]: #count occurences of each distinct digit
                    counter += 1
                    i += 1
                ans = ans + str(counter) + prev[i]  #as in the format requested: how many times 
                                                    # a digit appears, then the digit itself
                i += 1
            if i == l-1:
                ans = ans + str(1) + prev[i]
            return ans