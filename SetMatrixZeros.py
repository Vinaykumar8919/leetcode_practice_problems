class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        row = len(matrix)
        col = len(matrix[0])
        rowArray = []
        colArray = []
        for i in range(row):
            for j in range(col):
                if matrix[i][j]==0:
                    rowArray.append(i)
                    colArray.append(j)
        for i in set(rowArray):
            for j in range(col):
                matrix[i][j]=0
        for i in set(colArray):
            for j in range(row):
                matrix[j][i]=0
