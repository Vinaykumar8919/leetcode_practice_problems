# class Solution:
#     def champagneTower(self, poured: int, query_row: int, query_glass: int) -> float:
#         tower= [[0]*101 for _ in range(101)]
#         tower[0][0]=poured
#         for i in range(100):
#             for j in range(100):
#                 if tower[i][j]>=1:
#                     tower[i+1][j] += (tower[i][j]-1) / 2
#                     tower[i+1][j+1] += (tower[i][j]-1)/2
#                     tower[i][j] = 1
#         return tower[query_row][query_glass]


class Solution:
    def champagneTower(self, poured: int, query_row: int, query_glass: int) -> float:
        tower = [[0] * (i + 1) for i in range(query_row + 1)]
        tower[0][0] = poured

        for row in range(query_row):
            for glass in range(len(tower[row])):
                excess = (tower[row][glass] - 1) / 2.0
                if excess > 0:
                    tower[row + 1][glass] += excess
                    tower[row + 1][glass + 1] += excess

        return min(1.0, tower[query_row][query_glass])
