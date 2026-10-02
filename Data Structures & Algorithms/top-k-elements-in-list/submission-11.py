class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        freqMap = defaultdict(int)
        for n in nums:
            freqMap[n] += 1
        freq = [[] for _ in range(len(nums) + 1)]
        for num, count in freqMap.items():
            freq[count].append(num)
        res = []
        i = len(nums) - 1
        while k:
            if freq[i]:
                res.extend(freq[i])
                k -= len(freq[i])
            i -= 1
        return res