class Solution:
    def maxProfit(self, prices: list[int]) -> int:
        if len(prices) < 2:
            return 0
        else:
            max_diff = 0
            min_val = prices[0]

            for i in prices[1:]:
                max_diff = max(max_diff,i-min_val)
                min_val = min(min_val,i)

        return max_diff
