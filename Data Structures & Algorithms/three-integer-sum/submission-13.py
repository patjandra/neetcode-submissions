class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        # [-1, 0, 1, 2, -1, -4] --> [-4, -1, -1, 0, 1, 2]
        # sort the list
        # for each number
            # target = -(number)
            # for i in range(len(nums) - 1)
                # hold left and right ptrs
                # compute left+right
                    # if target, sort, check if in output list, add to a list
                    # if <target, increment left
                    # if >target, increment right
        #return output

        nums.sort()
        output = []
        for i in range(len(nums)-2):
            if i > 0 and nums[i] == nums[i - 1]:
                continue
            left = i+1
            right = len(nums)-1
            target = -nums[i]
            while left < right:
                value = nums[left]+nums[right]

                if value > target:
                    right -= 1
                elif value < target:
                    left += 1
                else:
                    output.append([nums[i], nums[left], nums[right]])

                    left += 1
                    while left < right and nums[left] == nums[left-1]:
                        left += 1
        return output
                

        