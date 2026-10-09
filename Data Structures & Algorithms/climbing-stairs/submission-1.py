class Solution:
    def climbStairs(self, n: int) -> int:
        memo = {}

        def climb(s):
            if s <= 1:
                return 1
            
            if s in memo:
                return memo[s]
            
            memo[s] = climb(s-1) + climb(s-2)
            return memo[s]

        return climb(n)