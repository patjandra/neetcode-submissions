class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        differences = []

        if len(prices) < 2:
            return 0

        for i in range(len(prices)):
            for j in range(i + 1, len(prices)):
                differences.append(prices[j] - prices[i])

        largest_profit = max(differences)
        return max(largest_profit, 0)