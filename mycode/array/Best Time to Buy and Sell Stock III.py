class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        N = len(prices)
        if N < 2:
            return 0
        start_max_profit = [0] * (N + 1)
        end_max_profit = [0] * N
        mx = prices[-1]
        for i in range(N - 1, -1, -1):
            mx = max(prices[i], mx)
            start_max_profit[i] = max(mx - prices[i], start_max_profit[i + 1])

        minx = prices[0]
        last = 0
        for i in range(N):
            minx = min(prices[i], minx)
            end_max_profit[i] = max(prices[i] - minx, last)
            last = end_max_profit[i]

        max_profit = 0
        for i in range(N):
            temp = end_max_profit[i] + start_max_profit[i + 1]
            if temp > max_profit:
                max_profit = temp
        return max_profit