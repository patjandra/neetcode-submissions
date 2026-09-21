class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        freqS = {}
        freqT = {}
        for i in s:
            freqS[i] = freqS.get(i, 0) + 1
        for i in t:
            freqT[i] = freqT.get(i, 0) + 1
        return freqS == freqT