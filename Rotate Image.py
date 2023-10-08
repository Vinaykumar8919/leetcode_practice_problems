# class Solution:
#     def rotate(self, matrix):
#         n = len(matrix)
#         extra = [[0] * n for _ in range(n)]
#         for i in range(n):
#             for j in range(n):
#                 extra[i][j] = matrix[i][j]
        
#         for i in range(n):
#             for j in range(n):
#                 matrix[j][n - i - 1] = extra[i][j]


class Solution:
    def rotate(self, matrix):
        n = len(matrix)
        for i in range(n):
            for j in range(i, n):
                matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]
        for i in range(n):
            matrix[i]=matrix[i][::-1]
    
