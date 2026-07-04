class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        
        if len(s) != len(t):
            return False

        seen1 = {}
        seen2 = {}

        for i in range(len(s)):
            if s[i] in seen1:
                seen1[s[i]] += 1
            else:
                seen1[s[i]] = 1
        for i in range(len(t)):
            if t[i] in seen2:
                seen2[t[i]] += 1
            else:
                seen2[t[i]] = 1
        return seen1 == seen2