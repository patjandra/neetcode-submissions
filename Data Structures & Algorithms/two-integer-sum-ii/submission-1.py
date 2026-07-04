class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        # binary search approach
        # compare middle item to target (want to only work with numbers less that target)
            # if item >= target, work with slice from [0:middle-index]
            # if item < target, begin comparing sums (should be from last 0:middle-index)
                # (naive/not-efficient) for each num, add with each num and check forward
        for i in range(len(numbers)):
            for j in range(len(numbers)):
                if numbers[i] + numbers[j] == target:
                    return [i+1, j+1]
                
