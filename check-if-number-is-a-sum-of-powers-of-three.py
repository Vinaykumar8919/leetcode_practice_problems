# class Solution:
#     def checkPowersOfThree(self, n: int) -> bool:
#         powers3 = [3 ** i for i in range(20)]
#         listLessThanN = [x for x in powers3 if x<=n]
#         print(listLessThanN)
#         while listLessThanN:
#             n = n - listLessThanN[-1]
#             listLessThanN.pop()
#             listLessThanN = [x for x in listLessThanN if x<=n]
#             print(listLessThanN, n)
#         if n==0:
#             return True
#         return False
        
            

            
class Solution:
    def checkPowersOfThree(self, n: int) -> bool:
        for i in range(15, -1, -1):
            ThreePowerI = pow(3, i)
            if n-ThreePowerI>=0:
                n=n-ThreePowerI
            if n==0:
                return True
        return False
        
            

            


