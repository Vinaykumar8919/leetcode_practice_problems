class Solution:
    def isPalindrome(self, s: str) -> bool:
        s1 = ''
        for i in s:
            if i.isalnum():
                s1 += i
        s1 = s1.lower()
        revs1 = s1[::-1]
        return s1 == revs1
