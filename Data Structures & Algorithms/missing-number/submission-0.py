class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        req = [i for i in range(len(nums)+1)]
        for num in req:
            if num not in nums:
                return num

            