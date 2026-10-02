class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        freqMap = defaultdict(int)
        for n in nums:
            freqMap[n] += 1
        freq = [[] for _ in range(len(nums) + 1)]
        for num, count in freqMap.items():
            freq[count].append(num)
        freq.reverse()
        res = []
        i = 0
        while k:
            if freq[i]:
                res.extend(freq[i])
                k -= len(freq[i])
            i += 1
        return res