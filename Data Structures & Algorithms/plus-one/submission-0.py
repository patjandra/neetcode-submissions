class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        num = ""
        for i in digits:
            num += str(i)
        num = int(num)+1
        return [int(str(num)[i]) for i in range(len(str(num)))]