class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        # counts = [0]*(len(nums)+1)
        # for i in range(len(nums)):
        #     counts[nums[i]]=counts[nums[i]]+1
        # print(counts)
        # for i in range(len(counts)):
        #     if counts[i]>1:
        #         return i
        
        res = slow = fast = 0
        while True:
            slow = nums[slow]
            fast = nums[nums[fast]]
            if fast==slow:
                break
        while res!=slow:
            slow = nums[slow]
            res = nums[res]
        return res
        
