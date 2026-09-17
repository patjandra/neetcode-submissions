class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        # sort the list
        # set complement of a num to be the target
        # search the remainder of the list to add up to complement
        out = []
        nums.sort()
        for i in range(len(nums)-2):
            if i > 0 and nums[i] == nums[i - 1]:
                continue
            target = -nums[i]
            left, right = i+1, len(nums)-1
            while left < right:
                if nums[left]+nums[right] < target:
                    left += 1
                elif nums[left]+nums[right] > target:
                    right -= 1
                else:
                    out.append([-target, nums[left], nums[right]])
                    left += 1
                    right -= 1
                    while left < right and nums[left] == nums[left-1]:
                        left += 1
                    while left < right and nums[right] == nums[right+1]:
                        right -= 1
        return out