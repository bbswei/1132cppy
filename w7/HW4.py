'''
>>> Input
A single line containing space-separated integers representing the stock prices over n days 
# 1 ≤ n ≤ 10^5
# 0 ≤ price[i] ≤ 10^3
For example: 7 1 5 3 6 4
 
>>> Output
A single integer representing the maximum profit that can be achieved.
If no profit is possible, return 0
'''

def main():
    money = map(int, input().split(" "))

    prices = []
    profits = []
    for spend in money:
        prices.append(spend)
        # print(prices)
        earn = spend - min(prices)
        profits.append(earn)
        # print(profit)
        max_profit = max(profits)
    
    print(max_profit)

if __name__ == '__main__':
    main()
