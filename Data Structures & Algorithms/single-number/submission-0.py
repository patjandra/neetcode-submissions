class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        freq = {}
        for i in nums:
            if i in freq:
                freq[i] += 1
            else:
                freq[i] = 1
        items = list(freq.items())
        for i in items:
            if i[1] == 1:
                return i[0]