class Solution:
    def trap(self, height: List[int]) -> int:
        leftMax = [0]
        curLeftMax = 0
        for i in range(1, len(height)):
            curLeftMax = max(curLeftMax, height[i-1])
            leftMax.append(curLeftMax)
        print("leftMax:", leftMax)

        rightMax = []
        curRightMax = 0
        for i in range(len(height)-2, -1, -1):
            curRightMax = max(curRightMax, height[i+1])
            rightMax.append(curRightMax)
        lst = rightMax[::-1]
        lst.append(0)
        print("rightMax:", lst)

        mins = [min(x, y) for x, y in zip(leftMax, lst)]
        print("mins", mins)

        water = 0
        for i in range(len(height)):
            if mins[i]-height[i] < 1:
                continue
            else:
                water += mins[i]-height[i]
        return water
            
        