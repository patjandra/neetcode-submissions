class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        freqMap = defaultdict(int)
        for n in nums:
            freqMap[n] += 1
        freq = [[] for _ in range(len(nums) + 1)]
        for num, count in freqMap.items():
            freq[count].append(num)
        res = []
        for count in range(len(nums), 0, -1):
            for num in freq[count]:
                res.append(num)
                if len(res) == k:
                    return res