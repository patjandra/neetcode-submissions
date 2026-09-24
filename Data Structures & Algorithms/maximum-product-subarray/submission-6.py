class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        currMax, currMin = 1, 1
        res = nums[0]
        for num in nums:
            curr = currMax * num
            currMax = max(currMin*num, curr, num)
            currMin = min(currMin*num, curr, num)
            res = max(res, currMax)
        return res