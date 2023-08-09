# class Solution:
#     def longestConsecutive(self, nums: List[int]) -> int:
#         if not nums:
#             return 0
#         nums_set = set(nums)
#         longest = 1
#         for i in nums:
#             count = 1
#             ele = i+1
#             while True:
#                 if ele not in nums_set:
#                     break
#                 count+=1
#                 ele+=1
#             longest = max(longest,count)
#         return longest



class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if not nums:
            return 0
        nums = set(nums)
        nums = sorted(nums) 
        maxcount = 1
        count = 1
        for i in range(len(nums) - 1):
            if nums[i] + 1 == nums[i + 1]:
                count += 1
            else:
                maxcount = max(maxcount, count)
                count = 1
        maxcount = max(maxcount, count)
        return maxcount

