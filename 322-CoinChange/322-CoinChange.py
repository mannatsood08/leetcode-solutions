class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        dp = [float('inf')]*(amount+1)
        dp[0] = 0
        for i in range(len(coins)):
            cur = [float('inf')]*(amount+1)
            for amt in range(amount+1):
                skip = dp[amt]
                notskip = float('inf')
                if amt-coins[i]>=0:
                    notskip = 1 + cur[amt-coins[i]]
                cur[amt] = min(notskip,skip)
            dp = cur
        return dp[amount] if dp[amount]!=float('inf') else -1