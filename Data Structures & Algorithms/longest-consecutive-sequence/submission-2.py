class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if len(nums) == 0:
            return 0

        nums.sort()
        streak = 1
        lst = []
        print(nums)
        for i in range(len(nums) - 1):
            if nums[i] == nums[i + 1]:
                continue
            elif nums[i] == nums[i + 1] - 1:
                streak += 1
            else:
                lst.append(streak)
                streak = 1
        lst.append(streak)
        return max(lst)
            