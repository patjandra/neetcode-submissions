class Solution:

    def encode(self, strs: List[str]) -> str:
        # [hello, hello] --> 5#hello5#hello
        encoding = ""
        for word in strs:
            encoding += str(len(word)) + '#' + word
        return encoding

    def decode(self, s: str) -> List[str]:
        lst = []
        i = 0
        
        while i < len(s):
            word = ""
            num = ""
            while s[i] != "#":
                num += s[i]
                i += 1
            j = i + 1
            wordEnd = int(num) + j
            while j < wordEnd:
                word += s[j]
                j += 1
            lst.append(word)
            i += int(num) + 1
        return lst
        
            
            
            