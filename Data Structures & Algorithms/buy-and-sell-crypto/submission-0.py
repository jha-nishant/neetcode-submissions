class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        ## look from the right to find the sell price
        # maxPrices = [0] * len(prices)
        # for i in range(len(prices) - 1, -1, -1):
        #     if i == len(prices) - 1:
        #         maxPrices[i] = prices[i]
        #     else:
        #         maxPrices[i] = max(maxPrices[i + 1], prices[i])
        # profit = 0
        # for index, price in enumerate(prices):
        #     if index == len(prices) - 1:
        #         continue
        #     cost = maxPrices[index + 1] - price
        #     profit = max(profit, cost)
        
        # return profit
        min_price = prices[0]
        max_profit = 0
        for index, price in enumerate(prices):
            if index > 0:
                cost = price - min_price
                max_profit = max(max_profit, cost)
                min_price = min(min_price, price)
        return max_profit


