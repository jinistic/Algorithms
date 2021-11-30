class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        profit = 0
        min_price = float("inf")

        for price in prices:
            min_price = min(min_price, price)
            profit = max(profit, price - min_price)

        return profit

        # min_price = float("inf")
        # max_price = -1
        # max_profit = 0
        # for price in prices:
        #     if price < min_price:
        #         if max_price - min_price > max_profit:
        #             max_profit = max_price - min_price

        #         min_price = price
        #         max_price = price

        #     if price > max_price:
        #         max_price = price

        # if max_price - min_price > max_profit:
        #     max_profit = max_price - min_price

        # return max_profit


sol = Solution()
print(sol.maxProfit(prices=[7, 1, 5, 3, 6, 4]))
print(sol.maxProfit(prices=[7, 6, 4, 3, 1]))
