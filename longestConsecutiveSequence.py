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



# class Solution:
#     def longestConsecutive(self, nums: List[int]) -> int:
#         if not nums:
#             return 0
#         nums = set(nums)
#         nums = sorted(nums) 
#         maxcount = 1
#         count = 1
#         for i in range(len(nums) - 1):
#             if nums[i] + 1 == nums[i + 1]:
#                 count += 1
#             else:
#                 maxcount = max(maxcount, count)
#                 count = 1
#         maxcount = max(maxcount, count)
#         return maxcount



class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        nums_set = set(nums)
        ans = 0
        for i in range(len(nums)):
            current_element = nums[i]
            count = 0
            previous_element = current_element-1
            if previous_element not in nums_set: # finding smallest  element in the chain
                while current_element in nums_set:
                    current_element+=1
                    count+=1
            ans = max(ans,count)
        return ans




        
