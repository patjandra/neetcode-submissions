class Solution:
    def maxArea(self, heights: List[int]) -> int:
        largestArea = 0
        for i in range(len(heights) - 1):
            for j in range(i+1, len(heights)):
                area = (min(heights[i], heights[j]))*(j - i)
                if (min(heights[i], heights[j]))*(j - i) > largestArea:
                    largestArea = area
        return largestArea