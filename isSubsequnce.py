class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        lengthofS = len(s)
        lengthofT = len(t)
        index1 = 0
        index2 = 0
        while index1 < lengthofS and index2 < lengthofT:
            if s[index1] == t[index2]:
                index1 += 1
            index2 += 1
        if index1==lengthofS:
            return 1
        return 0

        
