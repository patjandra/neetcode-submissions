class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        # got a freqMap of all values
        # create a list of freqMap pairs, but reverse to (count, num)
        # heapify the list (smallest counts to the top)
        # pop from heap til size k

        freqMap = defaultdict(int)
        for n in nums:
            freqMap[n] += 1
        heap = [(count, num) for num, count in freqMap.items()]
        heapq.heapify(heap)
        while len(heap) > k:
            heapq.heappop(heap)
        return [tup[1] for tup in heap]