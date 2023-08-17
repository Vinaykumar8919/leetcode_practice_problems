def checkvalid(i,j,m,n):
    if(i<0 or j<0 or i>=m or j>=n):
        return False
    return True

class Solution:
    def updateMatrix(self, mat: List[List[int]]) -> List[List[int]]:
        m = len(mat)
        n = len(mat[0])
        res = [[-1]*n for _ in range(m)]
        queue = []
        for i in range(m):
            for j in range(n):
                if mat[i][j]==0:
                    res[i][j]=0
                    queue.append([i,j])
        #BFS
        while queue:
            i = queue[0][0]
            j = queue[0][1]
            # check for its neighbour, if they are valid & not visited , then add them to queue
            if checkvalid(i+1,j,m,n) and res[i+1][j]==-1:
                queue.append([i+1,j])
                res[i+1][j]=res[i][j]+1
            if checkvalid(i-1,j,m,n) and res[i-1][j]==-1:
                queue.append([i-1,j])
                res[i-1][j]=res[i][j]+1
            if checkvalid(i,j+1,m,n) and res[i][j+1]==-1:
                queue.append([i,j+1])
                res[i][j+1]=res[i][j]+1
            if checkvalid(i,j-1,m,n) and res[i][j-1]==-1:
                queue.append([i,j-1])
                res[i][j-1]=res[i][j]+1
            queue.pop(0)
        return res
