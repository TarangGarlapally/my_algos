class Solution:
    def solve(self, prices, n):
        #unbounded knapsack
        profit = [0 for _ in range(n+1)]

        for i in range(n+1):
            for j in range(len(prices)):
                if( j+1 <= i):
                    profit[i] = max(profit[i], profit[i-(j+1)]+prices[j])
        return profit[-1]

