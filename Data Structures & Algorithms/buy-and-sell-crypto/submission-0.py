class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        min_till_now = sys.maxsize
        profit = 0
        for price in prices:
            profit = max(profit, price-min_till_now) 
            min_till_now = min(min_till_now, price)

        return profit