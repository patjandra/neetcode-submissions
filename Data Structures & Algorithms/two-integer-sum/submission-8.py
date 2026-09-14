class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        mapper = {}
        for i in range(len(nums)):
            mapper[nums[i]] = i
        for i in range(len(nums)):
            needed = target - nums[i]
            if needed in mapper and mapper[needed] != i:
                return [i, mapper[needed]]