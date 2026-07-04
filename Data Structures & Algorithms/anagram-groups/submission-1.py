class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        anagrams = defaultdict(list)
        for word in strs:
            sort = ''.join(sorted(word))
            if sort in anagrams:
                anagrams[sort].append(word)
            else:
                anagrams[sort] = [word]
        return list(anagrams.values())