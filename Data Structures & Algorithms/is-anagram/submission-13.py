class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        s1 = defaultdict(int)
        s2 = defaultdict(int)
        for i in s:
            s1[i] += 1
        for i in t:
            s2[i] += 1
        print(s1)
        print(s2)
        return s1 == s2