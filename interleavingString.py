class Solution:
    def isInterleave(self, s1: str, s2: str, s3: str) -> bool:
        if len(s2)+len(s1)!=len(s3):
            return False
        dp = [[False] * (len(s2)+1) for _ in range(len(s1)+1)]
        dp[0][0] = True
        for i in range(1, len(s1) + 1):
            dp[i][0] = dp[i-1][0] and s3[i-1] == s1[i-1]
            
        for j in range(1, len(s2) + 1):
            dp[0][j] = dp[0][j-1] and s3[j-1] == s2[j-1]
            
            
        for i in range(1,len(s1)+1):
            for j in range(1,len(s2)+1):
                dp[i][j] = (dp[i-1][j] and s3[i+j-1] == s1[i-1]) or \
                           (dp[i][j-1] and s3[i+j-1] == s2[j-1])
                    
        return dp[len(s1)][len(s2)]
        









# class Solution:
#     def isInterleave(self, s1: str, s2: str, s3: str) -> bool:
#         if len(s1) + len(s2) != len(s3):
#             return False
        
#         return self.isInterleaveRecursive(s1, s2, s3, 0, 0, 0)
    
#     def isInterleaveRecursive(self, s1, s2, s3, i, j, k):
#         if k == len(s3):
#             return True
#         if i < len(s1) and s1[i] == s3[k]:
#             if self.isInterleaveRecursive(s1, s2, s3, i + 1, j, k + 1):
#                 return True
#         if j < len(s2) and s2[j] == s3[k]:
#             if self.isInterleaveRecursive(s1, s2, s3, i, j + 1, k + 1):
#                 return True
#         return False


# class Solution:
#     def isInterleave(self, s1: str, s2: str, s3: str) -> bool:
#         if len(s1) + len(s2) != len(s3):
#             return False
        
#         i, j, k = 0, 0, 0
        
#         while k < len(s3):
#             if i < len(s1) and s1[i] == s3[k]:
#                 i += 1
#                 k += 1
#             elif j < len(s2) and s2[j] == s3[k]:
#                 j += 1
#                 k += 1
#             else:
#                 return False
        
#         return True







