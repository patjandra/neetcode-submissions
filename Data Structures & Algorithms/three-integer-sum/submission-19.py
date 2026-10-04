class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        # [-4, -1, -1, 0, 1, 5]
        # sort list
        # iterate through nums
        # if num is not first and is same as previous, continue to next num
        # two pointers, left (one ahead) and right (end)
        # if they sum to 0, add to output
            # increment left
            # while left equals left-1, increment
        # if the sum is less than zero increment left
        # if the sum is greater than zero decrement right
        nums.sort()
        out = []
        for i in range(len(nums)-1):
            l, r = i+1, len(nums)-1
            if i > 0 and nums[i] == nums[i-1]:
                continue
            while l < r:
                sm = nums[i] + nums[l] + nums[r]
                if sm == 0:
                    out.append([nums[i], nums[l], nums[r]])
                    l += 1
                    while l < len(nums) and nums[l] == nums[l-1]:
                        l += 1
                elif sm < 0:
                    l += 1
                else:
                    r -= 1
        return out