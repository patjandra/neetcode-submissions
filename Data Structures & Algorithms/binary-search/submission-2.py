class Solution:
    def search(self, nums: List[int], target: int) -> int:
        middle = nums[len(nums)//2]
        if target == middle:
            return len(nums)//2
        elif target > middle:
            for i in range(len(nums)//2, len(nums)):
                if target == nums[i]:
                    return i
            return -1
        elif target < middle:
            for i in range(len(nums)//2):
                if target == nums[i]:
                    return i
            return -1
        else:
            return -1


        