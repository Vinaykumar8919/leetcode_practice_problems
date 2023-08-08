
class Solution:
    def getRow(self, numRows: int) -> List[List[int]]:
       
        if numRows==0:
            return list([1])
        numRows+=1
        res=[]
        prev = [1]
        for i in range(1,numRows):
            currentRow = []
            currentRow.append(1)
            for j in range(1,i):
                currentRow.append(prev[j-1]+prev[j])
            currentRow.append(1)
            res=currentRow
            prev=currentRow
        return res



