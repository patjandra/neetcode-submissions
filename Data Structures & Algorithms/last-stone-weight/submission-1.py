class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        while len(stones) > 1:
            stones.sort()
            print(stones)
            if stones[len(stones)-1] == stones[len(stones)-2]:
                stones.pop()
                stones.pop()
            elif stones[len(stones)-1] < stones[len(stones)-2]:
                stones[len(stones)-2] -= stones[len(stones)-1]
                stones.pop()
            else:
                stones[len(stones)-1] -= stones[len(stones)-2]
                stones.pop(len(stones)-2)
        if len(stones) > 0:
            return stones[0]
        return 0