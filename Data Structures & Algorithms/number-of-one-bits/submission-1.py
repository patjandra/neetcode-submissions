class Solution:
    def hammingWeight(self, n: int) -> int:
        count = 0
        while n:    
            last = n&1
            if last == 1:
                count += 1
            n >>= 1
        return count