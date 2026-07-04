class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        #make an empty list
        #loop over each num
        #inner loop over each num
        #if equal, continue to the next iteration
        #if num[outer] + num[inner] == target, add outer, inner into empty list

        indices = []

        for i in range(len(nums)):
            for j in range(i + 1, len(nums)):
                if i != j and nums[i] + nums[j] == target:
                    indices += i, j
        return indices
                    
                