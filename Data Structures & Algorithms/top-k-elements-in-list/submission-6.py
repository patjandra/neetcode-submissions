class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        freq = defaultdict(int)
        for n in nums:
            freq[n] += 1
        freqLst = list(freq.items())
        srtLst = sorted(freqLst, key=lambda x:x[1], reverse=True)
        return [srtLst[i][0] for i in range(k)]