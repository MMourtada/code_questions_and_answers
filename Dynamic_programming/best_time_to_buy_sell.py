class Solution:
    
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        #Input is a list of prices of a given stock for per day
        #output is the max profit,
        #given that at most one trade is allowed(only one buy, and one sell at most)
        l = len(prices)
        if l <= 1:
            return 0     #if one day or none, no trade since we need at least two days
        else:
            profit = 0   #initiate the global variable profit
            while len(prices)>=2:    #since if less than two days, no trade
                if prices[-1] <= prices[-2]:
                    prices.pop()    #if the last day has a price less than the previous last, 
                                    #then it is not reasonable to sell at last day: get rid of it
                else:
                    profit = max(profit, prices[-1]-min(prices))  #else, sell at last price
                                             #assuming you buy at minimum price before the last day
                    prices.pop()   
                    #we got the candidate profit, now the last element is no more needed
                         
            return profit


       
      
        