class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        numDex = {}
        for i in range(len(numbers)):
            numDex[numbers[i]] = i
        for i in range(len(numbers)):
            complement = target-numbers[i]
            if complement in numDex and numDex[complement] != i:
                return [i+1, numDex[complement]+1]