class Solution:
    def isPalindrome(self, s: str) -> bool:
        clearStr = ""
        spaceless = s.replace(" ", "")
        for i in spaceless:
            if i.isalnum():
                clearStr += i.lower()
        reverse = clearStr[::-1]
        return clearStr == reverse
        