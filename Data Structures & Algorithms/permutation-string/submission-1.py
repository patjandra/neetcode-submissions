class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        s1 = sorted(s1)
        for i in range(len(s2)-len(s1)+1):
            perm = s2[i:i+len(s1)]
            perm = sorted(perm)
            if s1 == perm:
                return True
        return False