class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        res = [] # result list
        # intializing values
        left = 0
        right = len(matrix[0])
        top = 0
        bottom = len(matrix)
        while left < right and top <bottom:
            # get every element in top row
            for i in range(left,right):  # L -> R
                res.append(matrix[top][i])
            top+=1 

            #get every element in right column
            for i in range(top,bottom):   # T -> B
                res.append(matrix[i][right-1])
            right-=1
            # checking left reaches the right or top reaches the bottom

            if left>=right or top>=bottom:
                break
            
            #get every element in bottom row
            for i in range(right-1,left-1,-1):  # R -> L
                res.append(matrix[bottom-1][i])
            bottom-=1
           
           
            #get every element in left column
            for i in range(bottom-1,top-1,-1): # B -> T
                res.append(matrix[i][left])
            left+=1
        return res

    
