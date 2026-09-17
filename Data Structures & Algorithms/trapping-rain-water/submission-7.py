class Solution:
    def trap(self, height: List[int]) -> int:
        largestLeft, largestRight = 0, 0
        leftLst, rightLst = [0]*len(height), [0]*len(height)
        for i in range(len(height)):
            rightDex = len(height)-i-1
            largestLeft = max(largestLeft, height[i])
            largestRight = max(largestRight, height[rightDex])
            leftLst[i] = largestLeft
            rightLst[rightDex] = largestRight
        water = 0
        for i in range(len(height)):
            water += min(leftLst[i], rightLst[i]) - height[i]
        return water       