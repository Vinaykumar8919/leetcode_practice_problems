# class Solution:
#     def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
#         res = []
#         for i in range(len(nums)-k+1):
#             window=nums[i:i+k]
#             res.append(max(window))
#         return res

class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        res = []
        dequeue = []
        for i in range(len(nums)):
            while dequeue and nums[dequeue[-1]]<nums[i]:
                dequeue.pop()
            dequeue.append(i)
            while dequeue[0] <= i - k:
                dequeue.pop(0)
            if i>=k-1:
                res.append(nums[dequeue[0]])
        return res

            
