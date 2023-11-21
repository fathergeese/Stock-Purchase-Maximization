from functools import lru_cache
from itertools import combinations


# @lru_cache(maxsize=128)
def max_stocks(stocks_and_values, amount, memo={}):
    all_comb = []
    for r in range(2, len(stocks_and_values) + 1):
        comb = combinations(stocks_and_values, r)
        comb = list(comb)
        for c in comb:
            all_comb.append(c)
    for i in all_comb:
        total_stocks = 0
        value = 0
        for j in i:
            total_stocks += j[0]
            value += j[1]
        if value <= amount and value not in memo:
            memo[f'{i}'] = total_stocks
    max_stock_amount = max(memo.values())
    return max_stock_amount


stocks = [[1, 2], [4, 3], [5, 6], [6, 7]]
amount = 12
output = max_stocks(stocks, amount)
print(output)