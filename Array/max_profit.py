class Solution:
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        #initiate profit
        profit = 0
        #Need to buy at min and sell at next first local max price before it falls down again, 
   
         #the number of days in the list
             #if it's only one day profit is nul
          #will iterate thru the days
        buy = 0
        sell = 0
        i = 0
        l = len(prices)
        while i in range(l-1):
            if prices[i]<prices[i+1]:
                buy = prices[i]
                sell = prices[i+1]
                j = i+2
                while j in range(i+2, l):
                    if prices[j-1]<prices[j]:
                        sell = prices[j]
                        j += 1
                    else:
                        break
                profit += sell - buy
                i = j
            else:
                i += 1
               
        
        return profit