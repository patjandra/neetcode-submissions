class Solution:
    def longestPalindrome(self, s: str) -> str:
        longest = ""
        longestLen = 0

        for i in range(len(s)):
            l = r = i
            while l >= 0 and r < len(s) and s[l] == s[r]:
                curr = s[l:r+1]
                currLen = r - l + 1
                if currLen > longestLen:
                    longestLen = currLen
                    longest = curr
                l -= 1
                r += 1
        
        for i in range(len(s)):
            l, r = i, i+1
            while l >= 0 and r < len(s) and s[l] == s[r]:
                curr = s[l:r+1]
                currLen = r - l + 1
                if currLen > longestLen:
                    longestLen = currLen
                    longest = curr
                l -= 1
                r += 1
        return longest