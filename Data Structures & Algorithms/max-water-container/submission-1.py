class Solution:
    def maxArea(self, heights: List[int]) -> int:
        areaList = []
        for i in range(len(heights) - 1):
            for j in range(i+1, len(heights)):
                height = min(heights[i], heights[j])
                width = j - i
                areaList.append(height*width)
        return max(areaList)