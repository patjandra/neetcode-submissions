class Solution:
    def isHappy(self, n: int) -> bool:
        seen = set()
        num = n
        while num != 1:
            inter = 0
            for i in range(len(str(num))):
                inter += int(str(num)[i])**2
            if inter in seen:
                return False
            seen.add(inter)
            num = inter
        return True