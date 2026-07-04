class Solution:
    def reverseBits(self, n: int) -> int:
        out = 0
        for i in range(32):
            lastBit = n & 1
            out = (out<<1) | lastBit
            n >>= 1
        return out
        
        
        