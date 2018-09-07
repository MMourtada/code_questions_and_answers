class Solution:
    def isValidSudoku(self, board):
        """
        :type board: List[List[str]]
        :rtype: bool
        """
        #Input is a 9X9 Sudoku  (could have empty cells)
        #output is True or False according to whether the Sudoku is valid or not
        #Valid sudoku is such that: 
            #all rows contain the digits 1-9 without duplicates
            #all columns contain the digits 1-9 without duplicates  
            #all 9 3X3 sub-sudoku from top left to bottom right contain the digits1-9 without duplicates 

        from numpy import array  #importing array to handle slicing
        ans = True
        A = array(board)   #Easier to slice thru rows and colums
        for n in range(1, 10):  #iterating thru all digits from 1-9
            for i in range(9):   #iterating thru the rows and columns to check if duplicate exists
                if list(A[i,:]).count(str(n)) > 1 or  list(A[:,i]).count(str(n)) > 1:
                    ans = False
                    break
            if ans == False:
                break
            
            for j in range(3):                #Now atart to iterate thru the first 3 sub-blocks
                if (A[0:3,j*3:(j+1)*3] == str(n)).sum() > 1:
                    ans = False
                    break
            if ans == False:                  #iterate thru the next three sub-blocks
                break  
            for j in range(3,6):
                if (A[3:6,(j-3)*3:(j-2)*3] == str(n)).sum() > 1 :
                    ans = False
                    break
               
                        
            if ans == False:                   #iterate thru the last three subblocks
                break
            for j in range(6,9):
                if (A[6:9, (j-6)*3:(j-5)*3] == str(n)).sum() > 1 :
                    ans = False
                    break
             
            if ans == False:
                break
          
                
        return ans