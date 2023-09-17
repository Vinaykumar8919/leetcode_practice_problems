from collections import Counter
class Solution:
    def intersect(self, nums1: List[int], nums2: List[int]) -> List[int]:
        counts = Counter(nums1)
        res = []
        for ele in nums2:
            if counts[ele] > 0:
                res.append(ele)
                counts[ele] -= 1
        return res
