class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        maxMax, maxMin = 1, 1
        res = nums[0]
        for num in nums:
            curr = maxMax * num
            maxMax = max(maxMin*num, curr, num)
            maxMin = min(maxMin*num, curr, num)
            res = max(res, maxMax, maxMin)
        return res