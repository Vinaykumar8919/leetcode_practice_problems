class Solution:
    def reverseWords(self, s: str) -> str:
        words = s.split()
        words=words[::-1]
        res=""
        for i in words[:len(words)-1]:
            res=res+i+" "
        res+=words[-1]
        return res
