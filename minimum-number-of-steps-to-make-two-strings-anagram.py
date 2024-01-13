from collections import Counter
class Solution:
    def minSteps(self, s: str, t: str) -> int:
        sCounter = Counter(s)
        tCounter = Counter(t)
        res = 0
        for i in  sCounter.keys():
            
            temp = sCounter[i]-tCounter[i]
            print(sCounter[i], tCounter[i], temp)
            if temp>0:
                res+=temp
        return res

        
