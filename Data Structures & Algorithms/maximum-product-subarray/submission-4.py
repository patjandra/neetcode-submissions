class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        maxMax, maxMin = 1, 1
        res = nums[0]
        for num in nums: # -2, 3, -4
            curr = maxMax * num # -2, 3, -12
            maxMax = max(maxMin*num, curr, num) # 1, 3, -4
            maxMin = min(maxMin*num, curr, num) # -2, -6, -12

            res = max(res, maxMax, maxMin) # 1, 3, 
        return res