class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        freq = {}
        for num in nums:
            if num in freq:
                freq[num] += 1
            else:
                freq[num] = 1
        lst = [i for i in list(freq.items())]
        lst = sorted(lst, key=lambda x:x[1], reverse=True)
        return [lst[i][0] for i in range(k)]