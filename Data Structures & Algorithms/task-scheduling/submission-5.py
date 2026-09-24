class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        # A, B, C, *, A, *, *, *, A
        # X, Y, *, X, Y
        freq = {}
        for task in tasks:
            freq[task] = freq.setdefault(task, 0) - 1
        maxHeap = list(freq.values())
        heapq.heapify(maxHeap)
        cooldown = []
        time = 0
        while maxHeap or cooldown:
            if not maxHeap and cooldown:
                while not maxHeap:
                    if cooldown[0][1] == time: # if first item in queue cooldown done
                        heapq.heappush(maxHeap, cooldown[0][0])
                        cooldown.pop(0)
                    time += 1
            task = heapq.heappop(maxHeap) + 1 # increment since complete task
            if task: # if still tasks, put in cooldown
                cooldown.append((task, time + n))
            if cooldown:
                if cooldown[0][1] == time: # if first item in queue cooldown done
                    heapq.heappush(maxHeap, cooldown[0][0])
                    cooldown.pop(0)
            time += 1
        return time