class WordDictionary:

    def __init__(self):
        self.words = []

    def addWord(self, word: str) -> None:
        self.words.append(word)

    def search(self, word: str) -> bool:
        for wrd in self.words:
            if len(wrd) != len(word):
                continue
            i = 0
            while i < len(wrd):
                if word[i] == "." or word[i] == wrd[i]:
                    i+=1
                else:
                    break
            if i == len(wrd):
                return True
        return False
