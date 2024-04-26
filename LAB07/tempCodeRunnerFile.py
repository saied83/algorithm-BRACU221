def minNumbCoins(numCoins, totalAmount, coins):
#     dp = [[float('inf')] * (totalAmount+1) for _ in range(numCoins+1)]

#     for j in range(totalAmount+1):
#         dp[0][j] = 0

#     for i in range(1, numCoins+1):
#         dp[i][0] = 0
#         for j in range(1, totalAmount+1):
#             dp[i][j] = dp[i-1][j]
#             if j >= coins[i-1]:
#                 dp[i][j] = min(dp[i][j], dp[i][j-coins[i-1]] + 1)
#     print(dp)
#     if dp[numCoins][totalAmount] != float('inf'):
#         return dp[numCoins][totalAmount]
#     else:
#         return -1