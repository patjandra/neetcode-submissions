class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        while len(stones) > 1:
            stones.sort()
            h1 = stones[-1]
            h2 = stones[-2]
            if h1 == h2:
                stones.pop()
                stones.pop()
                continue
            if h1 < h2:
                stones[-2] -= h1
                stones.pop()
            else:
                stones[-1] -= h2
                stones.remove(h2)
        return stones[0] if stones else 0