class Solution:
    def generateMatrix(self, n: int) -> List[int]:
        res = [[0 for _ in range(n)] for _ in range(n)]
        # intializing values
        left = 0
        right =n
        top = 0
        bottom = n
        count=1
        while left < right and top <bottom:
            for i in range(left,right):  # L -> R
                res[top][i]=count
                count+=1
            top+=1 

            for i in range(top,bottom):   # T -> B
                res[i][right-1]=count
                count+=1
            right-=1
           

            if left>=right or top>=bottom:
                break
            
        
            for i in range(right-1,left-1,-1):  # R -> L
                res[bottom-1][i]=count
                count+=1
            bottom-=1
           
            for i in range(bottom-1,top-1,-1): # B -> T
                res[i][left]=count
                count+=1
            left+=1
        return res

    
