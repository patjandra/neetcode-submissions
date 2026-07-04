class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        # loop through len(s2)-len(s1)+1
            # grab slice i to i+len(s1)
            # sort s1 and slice with "".join(sorted(x))
            # if equal, return true
        # return false
        s1 = "".join(sorted(s1))
        for i in range(len(s2)-len(s1)+1):
            perm = s2[i:i+len(s1)]
            perm = "".join(sorted(perm))
            if s1 == perm:
                return True
        return False


