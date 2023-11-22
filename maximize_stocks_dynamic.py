from functools import lru_cache
from itertools import combinations


@lru_cache(maxsize=None)
def max_stocks(stocks_and_values, amount, memo={}):
    all_stock_subsets = []
    # Obtain all possible subsets of stock amounts and values
    for r in range(2, len(stocks_and_values) + 1):
        stock_subsets = combinations(stocks_and_values, r)
        stock_subsets = list(stock_subsets)
        for subset in stock_subsets:
            all_stock_subsets.append(subset)
    # Look for valid stock subset
    for i in all_stock_subsets:
        stock_amount= 0
        value = 0
        for j in i:
            stock_amount += j[0]
            value += j[1]
        if value <= amount and value not in memo:
            memo[f'{i}'] = stock_amount
    # Return the subset with the largest amount of stocks
    max_stock_amount = max(memo.values())
    return max_stock_amount


stocks = ((1, 2), (4, 3), (5, 6), (6, 7))
amount = 12
output = max_stocks(stocks, amount)
print(output)

stocks2 =  ((3, 2), (4, 3), (5, 3), (6, 7))
amount2 = 10
print(max_stocks(stocks2, amount2))
