def maxProfit(prices):
    minimumPrice = prices[0]
    maximumProfit = 0

    for i in range(1, len(prices)):
        currentPrice = prices[i]

        if currentPrice < minimumPrice:
            minimumPrice = currentPrice

        profit = currentPrice - minimumPrice

        if profit > maximumProfit:
            maximumProfit = profit

    return maximumProfit


# Input
prices = [7, 1, 5, 3, 6, 4]

# Function call
result = maxProfit(prices)

# Output
print("Maximum Profit:", result)