class Solution:
    def isPalindrome(self, s: str) -> bool:
        end = len(s)-1
        for front in range(len(s)):
            """
            if front > end:
                return True
            """
            if not s[front].isalnum():
                continue
            while not s[end].isalnum():
                end -= 1
            if s[front].lower() != s[end].lower():
                return False
            end -= 1
        return True
