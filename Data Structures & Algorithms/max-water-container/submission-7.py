class Solution:
    def maxArea(self, heights: List[int]) -> int:
        def area(left, right):
            return min(heights[left], heights[right]) * (right - left)
        
        left, right = 0, len(heights) - 1
        maxContainer = 0
        while left < right:
            maxContainer = max(maxContainer, area(left,right))
            if heights[left] <= heights[right]:
                left += 1
            else: 
                right -= 1
        
        return maxContainer
