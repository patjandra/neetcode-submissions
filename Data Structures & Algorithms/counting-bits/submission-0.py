class Solution:
    def countBits(self, n: int) -> List[int]:
        out = []
        for num in range(n+1):
            binary = bin(num)[2:]
            print(binary)
            count = 0
            for dig in binary:
                if int(dig) == 1:
                    count += 1
            out.append(count)
        return out