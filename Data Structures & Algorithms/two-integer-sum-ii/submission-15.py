class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        numDex = {}
        for i in range(len(numbers)):
            complement = target-numbers[i]
            if complement in numDex and numDex[complement] != i:
                return [min(i, numDex[complement])+1, max(i, numDex[complement])+1]
            numDex[numbers[i]] = i