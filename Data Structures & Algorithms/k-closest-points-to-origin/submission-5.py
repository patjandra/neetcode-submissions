class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        distPairs = [(-(math.sqrt((x**2)+(y**2))), (x, y)) for x, y in points]
        heapq.heapify(distPairs)
        while len(distPairs) > k:
            heapq.heappop(distPairs)
        return [(y[0], y[1]) for x, y in distPairs]