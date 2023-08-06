class Solution:
   def longestCommonPrefix(self,strs):
    if not strs:
        return ""
    min_str = min(strs)
    max_str = max(strs)
    
    res = ''
    for i in range(len(min_str)):
        if max_str[i]==min_str[i]:
            res=res+min_str[i]
        else:
            return res
    return res
