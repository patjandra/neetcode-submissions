class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        start, longest, currLength = 0, 0, 0
        seen = set()

        for i in range(len(s)):
            if s[i] in seen:
                while s[i] in seen:
                    seen.remove(s[start])
                    currLength -= 1
                    start += 1
                seen.add(s[i])
                currLength += 1
            else:
                seen.add(s[i])
                currLength += 1
                if currLength > longest:
                    longest = currLength
        return longest


        
        


        
            