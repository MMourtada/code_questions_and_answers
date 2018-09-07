class Solution:
    def rotate(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: void Do not return anything, modify matrix in-place instead.
        """

        #Input is a list of lists representing rows of an nXn matrix
        #Output is the 90-degree clockwise rotation of the image of this list of lists (aka its matrix)
        #The rotation is to be done in place
        n = len(matrix)
        # transposing the list
        for i in range(n):    #enough to work on the part of matrix under main diagonal
            for j in range(i):
                temp = matrix[i][j]
                matrix[i][j] = matrix[j][i]
                matrix[j][i] = temp
                
        # reflecting columns 
        
        for i in range(n):
            for j in range(n//2):
                temp = matrix[i][j]
                matrix[i][j] = matrix[i][n-1-j]
                matrix[i][n-1-j] = temp