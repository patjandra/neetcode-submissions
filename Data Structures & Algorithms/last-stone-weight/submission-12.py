class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        lst = [-n for n in stones]
        heapq.heapify(lst)
        while len(lst) > 1:
            h1 = -heapq.heappop(lst)
            h2 = -heapq.heappop(lst)
            if h1 != h2:
                heapq.heappush(lst, -(h1-h2))
        return -lst[0] if lst else 0