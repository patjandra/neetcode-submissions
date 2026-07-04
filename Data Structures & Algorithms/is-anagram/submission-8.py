class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        sTable = {}
        tTable = {}
        for i in s:
            sTable[i] = 1 + sTable.get(i, 0)
        for i in t:
            tTable[i] = 1 + tTable.get(i, 0)
        return sTable == tTable