class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        # each index in the output is the product of its prefix and postfix
        # e.g. index 0 = (1) * (2*4*6) | index 1 = (1) * (4*6) | index 2 = (1*2) * (6) | index 3 = (1*2*4) * (6)
        # create a prefix array (1, 1, 2, 8) and postfix array (24, 24, 6, 6)
        # [1, 2, 3, 4] --> [24, 12, 8, 6]
        # [1,1,2,6] n [1, 4,12,24]
        products = [1] * len(nums)
        prefix = [1] * len(nums)
        postfix = [1] * len(nums)
        
        prefix[0] = 1
        postfix[-1] = 1
        for i in range(1, len(nums)):
            prefix[i] = nums[i - 1] * prefix[i - 1]
        for i in range(len(nums) - 2, -1, -1):
            postfix[i] = nums[i + 1] * postfix[i + 1]
        for i in range(len(nums)):
            products[i] = prefix[i] * postfix[i]
        return products