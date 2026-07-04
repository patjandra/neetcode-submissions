class Solution:
    def reverse(self, x: int) -> int:
        if x < 0:
            x = str(x)[1:]
            reverse = "-" + x[::-1]
        else:
            reverse = str(x)[::-1]
        if -2**31 <= int(reverse) <= (2**31)-1:
            return int(reverse)
        return 0