class Solution:
    def champagneTower(self, poured: int, query_row: int, query_glass: int) -> float:
        tower= [[0]*101 for _ in range(101)]
        tower[0][0]=poured
        for i in range(100):
            for j in range(100):
                if tower[i][j]>=1:
                    tower[i+1][j] += (tower[i][j]-1) / 2
                    tower[i+1][j+1] += (tower[i][j]-1)/2
                    tower[i][j] = 1
        return tower[query_row][query_glass]
