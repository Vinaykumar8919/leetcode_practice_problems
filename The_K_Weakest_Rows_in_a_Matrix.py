'''
                program - 1
                using dictionary 
                         '''
class Solution:
    def kWeakestRows(self, mat: List[List[int]], k: int) -> List[int]:
        
        row = len(mat)
        col = len(mat[0])
        soliders = {}
        for i in range(row):
            soliders[i]=0
            for j in range(col):
                if mat[i][j]==1:
                    if i in soliders:
                        soliders[i]=soliders[i]+1
                    else:
                        soliders[i]=1

        # print(soliders)
        soliders = dict(sorted(soliders.items(), key=lambda x:x[1]))
        # print(soliders)
        res = list(soliders.keys())
        return res[:k]
        
        
                

        
