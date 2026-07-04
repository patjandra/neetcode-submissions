class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        longest = 0

        for i in range(len(s)):
            substring = ""
            count = defaultdict(int)
            for j in range(i, len(s)):
                substring += s[j]
                count[s[j]] += 1
                replacements = len(substring) - max(count.values())
                if replacements <= k:
                    longest = max(longest, len(substring))
        return longest








        