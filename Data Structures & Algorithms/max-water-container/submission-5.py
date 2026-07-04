class Solution:
    def maxArea(self, heights: List[int]) -> int:
        largestArea = 0
        left = 0
        right = len(heights) - 1
        while left < right:
            height = min(heights[left], heights[right])
            width = right - left
            currArea = height*width
            if currArea > largestArea:
                largestArea = currArea
            if heights[left] > heights[right]:
                right -= 1
            else:
                left += 1
        return largestArea