class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        start = 0
        nums.sort()
        for i in range(len(nums)):
            if nums[i] != start:
                return start
            start += 1
        return start