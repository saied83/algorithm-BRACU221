import sys

def minNumbCoins(coins, totalAmount):
    dp = [float('inf')] * (totalAmount + 1)
    dp[0] = 0

    for coin in coins:
        for i in range(coin, totalAmount + 1):
            dp[i] = min(dp[i], dp[i - coin] + 1)

    if dp[totalAmount]!= float('inf'):
        return dp[totalAmount]
    else:
        return -1



def main():
    sys.stdin = open('input4.txt', 'r')
    sys.stdout = open('output4.txt', 'w')
    n, x = list(map(int, input().split(" ")))
    coins = list(map(int, input().split(" ")))
    print(minNumbCoins(coins,x))
    

if __name__ == "__main__":
    main()