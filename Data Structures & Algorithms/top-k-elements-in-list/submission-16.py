class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        # build freq map
        # build buckets where each index represents the count
        # fill in buckets
        # iterate through buckets to fill in res list with k items

        freqMap = defaultdict(int)
        buckets = [[] for _ in range(len(nums)+1)]
        res = []

        for n in nums:
            freqMap[n] += 1
        for num, count in freqMap.items():
            buckets[count].append(num)
        for i in range(len(nums), 0, -1):
            for n in buckets[i]:
                res.append(n)
                if len(res) == k:
                    return res