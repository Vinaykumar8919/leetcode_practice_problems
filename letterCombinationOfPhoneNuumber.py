class Solution:
    def combination(self,list1,list2):
        res=[]
        if list1==[]:
            return list2
        else:
            res = [x + y for x in list1 for y in list2]
        return res


    def letterCombinations(self, digits: str) -> List[str]:
        numberAlph = {
            "2": ['a', 'b', 'c'],
            "3": ['d', 'e', 'f'],
            "4": ['g', 'h', 'i'],
            "5": ['j', 'k', 'l'],
            "6": ['m', 'n', 'o'],
            "7": ['p', 'q', 'r', 's'],
            "8": ['t', 'u', 'v'],
            "9": ['w', 'x', 'y', 'z']
        }
        res = []
        if digits =="":
            return res
        else:
            for i in digits:
                res = Solution().combination(res,numberAlph[i])
        return res
