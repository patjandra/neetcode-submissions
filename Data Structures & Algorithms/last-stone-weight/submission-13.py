class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        lst = [-s for s in stones]
        heapq.heapify(lst)
        while len(lst) > 1:
            s1, s2 = -heapq.heappop(lst), -heapq.heappop(lst)
            if s1 != s2:
                heapq.heappush(lst, -(s1-s2))
        return -lst[0] if lst else 0