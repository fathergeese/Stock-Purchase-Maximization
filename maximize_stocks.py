from functools import lru_cache
from itertools import combinations


@lru_cache(maxsize=128)
def max_stocks(stocks_and_values, amount, memo={}):
    all_stock_combinations = []
    # Obtain all possible combinations of stock amounts and values
    for r in range(2, len(stocks_and_values) + 1):
        stock_combination = combinations(stocks_and_values, r)
        stock_combination = tuple(stock_combination)
        for c in stock_combination:
            all_stock_combinations.append(c)
    # Look for valid stock combinations
    for i in all_stock_combinations:
        total_stocks = 0
        value = 0
        for j in i:
            total_stocks += j[0]
            value += j[1]
        if value <= amount and value not in memo:
            memo[f'{i}'] = total_stocks
    # Return the combination with the largest amount of stocks
    max_stock_amount = max(memo.values())
    return max_stock_amount


stocks = ((1, 2), (4, 3), (5, 6), (6, 7))
amount = 12
output = max_stocks(stocks, amount)
print(output)