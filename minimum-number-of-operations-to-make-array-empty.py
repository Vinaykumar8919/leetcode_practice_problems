class Solution:
    def fun(self, val):
        while val%3!=0:
            val+=1
        return val//3
    def minOperations(self, nums: List[int]) -> int:
        hash = dict()
        res = 0
        for i in nums:
            hash[i]=hash.get(i,0)+1

        for val in hash.values():
            if val==1:
                return -1
            else:
                res+=self.fun(val)
        return res
