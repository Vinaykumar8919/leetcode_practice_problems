class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        if numRows==0:
            return [[]]
        res=[]
        prev = [1]
        res.append(prev)
        for i in range(1,numRows):
            currentRow = []
            currentRow.append(1)
            for j in range(1,i):
                currentRow.append(prev[j-1]+prev[j])
            currentRow.append(1)
            res.append(currentRow)
            prev=currentRow
        return res



