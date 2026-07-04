class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        # loop through nums
        # for each num, multiply all values except when i = j


        products = []
        for i in range(len(nums)):
            product = 1
            for j in range(len(nums)):
                if i == j:
                    continue
                else:
                    product *= nums[j]
            products.append(product)
        return products
                    