class Solution:
    def romanToInt(self, s: str) -> int:
        symbol = {
            'I': 1,
            'V': 5,
            'X': 10,
            'L': 50,
            'C': 100,
            'D': 500,
            'M': 1000
        }
        res = 0
        prev = 0  # Move prev outside the loop
        for i in reversed(s):
            if symbol[i] >= prev:  # Compare symbol[i] with prev
                res = res + symbol[i]
            else:
                res = res - symbol[i]
            prev = symbol[i]  # Update prev for the next iteration
        return res
