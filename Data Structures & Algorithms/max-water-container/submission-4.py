class Solution:
    def maxArea(self, heights: List[int]) -> int:
        largestArea = 0
        for n in range(len(heights)):
            l = n
            r = n+1
            while r < len(heights):
                height = min(heights[l], heights[r])
                width = r - l
                if height*width > largestArea:
                    largestArea = height*width
                r += 1
            l += 1
        return largestArea
