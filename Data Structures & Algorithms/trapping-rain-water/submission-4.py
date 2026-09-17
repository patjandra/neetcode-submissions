class Solution:
    def trap(self, height: List[int]) -> int:
        # loop, store max seen so far in each index
        # [0, 2, 2, 3, 3, 3, 3, 3, 3, 3] left->right
            # [1, 2, 3, 3, 3, 3, 3, 3, 3, 3] right->left
        # [3, 3, 3, 3, 3, 3, 3, 3, 2, 1] reversed right->left
        # for each index, min(l1, l2) - height[index]
        largestLeft = 0
        largestRight = 0
        leftLst = []
        rightLst = []
        for i in range(len(height)):
            largestLeft = max(largestLeft, height[i])
            largestRight = max(largestRight, height[len(height)-i-1])
            leftLst.append(largestLeft)
            rightLst.append(largestRight)
        rightLst.reverse()
        water = 0
        for i in range(len(height)):
            water += min(leftLst[i], rightLst[i]) - height[i]
        return water       