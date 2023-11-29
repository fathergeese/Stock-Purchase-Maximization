from functools import lru_cache
from itertools import combinations


@lru_cache(maxsize=None)
def max_stocks(stocks_and_values: tuple, amount: float):
    memo = {}
    all_stock_subsets = []
    # Obtain all possible subsets of stock amounts and values
    for r in range(1, len(stocks_and_values) + 1):
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
        if value <= amount:
            memo[f'{i}'] = stock_amount
    # Return the subset with the largest amount of stocks
    if memo:
        max_stock_amount = max(memo.values())
    else:
        max_stock_amount = 0
    return max_stock_amount

with open("output2.txt", "w") as Outfile:                                                              
    with open('input.txt') as file:                                          
        
        # 1 different inputs
        for i in range(10):                                                  
            # Reads the max amount
            max_amount = int(file.readline().strip())               
            temp = file.readline().strip()[1:-1].split("],[")
            companies = []
            for j in temp:
                if j == '': # Company Stock list is empty
                    continue
                stocks, value = j.split(",")
                stocks = int(stocks)
                value = int(value)
                companies.append((stocks, value))
            
            # Constraint check
            companies = tuple(companies)
            if len(companies) >= 0 and len(companies) <= 100000:
                # Output 1
                number_of_stocks = max_stocks(companies, max_amount)
                Outfile.write(f"Input {i + 1}: Number of stocks = {number_of_stocks}\n")
            else:
                Outfile.write("Sorry, this input is invalid.\n")
        print("\nResults written to output2.txt\n") 
