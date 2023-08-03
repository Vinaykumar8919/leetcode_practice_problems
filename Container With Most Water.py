# link https://leetcode.com/problems/container-with-most-water/description/
class Solution:
    def maxArea(self, height: List[int]) -> int:
        left = 0
        right = len(height)-1
        water =  min(height[left],height[right]) *  (right-left)
        while left<right:
            if height[left]<height[right]:
                left+=1
            else:
                right-=1
            volume = min(height[left],height[right]) *  (right-left)
            if volume>water:
                water = volume
        return water
