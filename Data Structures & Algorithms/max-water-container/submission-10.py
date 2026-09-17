class Solution:
    def maxArea(self, heights: List[int]) -> int:
        maxArea = 0
        l, r = 0, len(heights) - 1
        while l < r:
            lCol, rCol = heights[l], heights[r]
            maxArea = max(maxArea, min(lCol, rCol) * (r - l))
            if lCol <= rCol:
                l += 1
            else:
                r -= 1
        return maxArea