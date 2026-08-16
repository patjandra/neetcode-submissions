class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        points = [[x**2 + y**2, [x, y]] for x, y in points]
        heapq.heapify(points)
        return [heapq.heappop(points)[1] for _ in range(k)]