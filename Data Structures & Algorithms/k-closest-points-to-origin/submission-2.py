class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        points = [[math.sqrt((x-0)**2 + (y-0)**2), [x, y]] for x, y in points]
        heapq.heapify(points)
        return [heapq.heappop(points)[1] for _ in range(k)]