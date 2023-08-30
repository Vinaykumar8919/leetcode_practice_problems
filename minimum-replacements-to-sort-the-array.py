class Solution:
    def minimumReplacement(self, A: List[int]) -> int:
        n = len(A)
        res = 0
        prev = A[n-1]
        for i in range(n-2, -1, -1):
            if A[i]>prev:
                k = math.ceil(A[i]/prev)
                res+=k-1
                prev = A[i]//k
            else:
                prev = A[i]
        return res
