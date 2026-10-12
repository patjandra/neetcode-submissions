class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        # at each call, I have the option to include the int or not
        # I need to explore both paths and add each intermediary result to output list

        out = []

        subset = []
        def backtrack(i):
            if i == len(nums):
                out.append(subset.copy())
                return
            subset.append(nums[i])
            backtrack(i+1)
            subset.pop()
            backtrack(i+1)
        backtrack(0)

        return out