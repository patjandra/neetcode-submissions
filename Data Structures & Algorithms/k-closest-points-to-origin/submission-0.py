class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        lst = []
        for point in points:
            distance = math.sqrt(((point[0]-0)**2)+((point[1]-0)**2))
            lst.append((distance,point))
        lst.sort()
        out = []
        for i in range(k):
            out.append(lst[i][1])
        return out