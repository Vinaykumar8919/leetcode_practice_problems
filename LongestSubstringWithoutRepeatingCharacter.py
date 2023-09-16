class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        start = 0
        end = 0
        n = len(s)
        unique = set()  
        Max = 0 
        while end < n:
            if s[end] not in unique:
                unique.add(s[end])
                end += 1
                Max = max(Max, end - start)  
            else:
                unique.remove(s[start])
                start += 1
        return Max
