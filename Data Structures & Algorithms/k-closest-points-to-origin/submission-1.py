class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        points = [[math.sqrt((x-0)**2 + (y-0)**2), [x, y]] for x, y in points]
        heapq.heapify(points)
        kClosest = []
        for i in range(k):
            point = heapq.heappop(points)
            kClosest.append(point[1])
        return kClosest