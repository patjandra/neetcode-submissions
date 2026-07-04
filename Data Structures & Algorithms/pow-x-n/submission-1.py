class Solution:
    def myPow(self, x: float, n: int) -> float:
        total = 1
        if n < 0:
            while n:
                total *= 1/x
                n += 1
            return total
        while n:
            total *= x
            print(total, n)
            
            n -= 1
        return total
        