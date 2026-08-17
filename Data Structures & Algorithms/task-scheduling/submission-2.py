class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        freq = Counter(tasks)
        heap = [-cnt for cnt in freq.values()]
        heapq.heapify(heap)
        q = deque()
        time = 0

        while heap or q:
            time += 1
            if not heap:
                time = q[0][1]
            else:
                cnt = heapq.heappop(heap) + 1
                if cnt:
                    q.append((cnt, time + n))
            if q and q[0][1] == time:
                heapq.heappush(heap, q.popleft()[0])
        return time