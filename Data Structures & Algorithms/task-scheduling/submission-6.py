class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        freq = {}
        for task in tasks:
            freq[task] = freq.setdefault(task, 0) - 1
        maxHeap = list(freq.values())
        heapq.heapify(maxHeap)
        cooldown = deque()
        time = 0
        while maxHeap or cooldown:
            if not maxHeap and cooldown:
                while not maxHeap:
                    if cooldown[0][1] == time: # if first item in queue cooldown done
                        heapq.heappush(maxHeap, cooldown[0][0])
                        cooldown.popleft()
                    time += 1
            task = heapq.heappop(maxHeap) + 1 # increment since complete task
            if task: # if still tasks, put in cooldown
                cooldown.append((task, time + n))
            if cooldown:
                if cooldown[0][1] == time: # if first item in queue cooldown done
                    heapq.heappush(maxHeap, cooldown[0][0])
                    cooldown.popleft()
            time += 1
        return time