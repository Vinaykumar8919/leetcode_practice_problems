# class Solution:
#     def minDeletions(self, s: str) -> int:
#         letter_count = {}
#         for i in s:
#             if i in letter_count:
#                 letter_count[i]+=1
#             else:
#                 letter_count[i]=1
#         temp = []
#         for i in letter_count.values():
#             temp.append(i)          
#         res = 0
#         print(temp)
#         for index, ele in enumerate(temp):
#             while temp[index] in set(temp[:index]+temp[index+1:]):
#                 temp[index]-=1 
#                 if temp[index]==0:
#                     del temp[index]
#                 res +=1 
#         return res
class Solution:
    def minDeletions(self, s: str) -> int:
        letter_count = {}
        for i in s:
            if i in letter_count:
                letter_count[i]+=1
            else:
                letter_count[i]=1
        # temp = []
        # for i in letter_count.values():
        #     temp.append(i)
        res = 0
        # print(temp)
        unique = set()
        for ele in letter_count.values():
            while ele in unique:
                ele-=1 
                res +=1
            if ele!=0:
                unique.add(ele)
        return res
