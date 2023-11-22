# Max Stocks Finder

This Python script (`max_stocks_dynamic.py`) finds the maximum number of stocks you can buy with a given amount of money. It explores all possible subset of stocks and returns the maximum number of stocks that can be bought without exceeding the specified amount.

## Usage

1. **Input:**
    - Modify the `stocks` tuple to represent the available stocks. Each stock should be a tuple of two elements: the first element is the number of stocks available, and the second element is the value of each stock.
    ```python
    stocks = ((1, 2), (4, 3), (5, 6), (6, 7))
    ```

    - Adjust the `amount` variable to the amount of money you have.
    ```python
    amount = 12
    ```

2. **Run the script:**
    - Execute the script in your Python environment.
    ```bash
    python max_stocks_dynamic.py
    ```

3. **Output:**
    - The script will print the maximum number of stocks that can be bought with the given amount.
    ```python
    output = max_stocks(stocks, amount)
    print(output)
    ```

### Alan Campos - argelalan@csu.fullerton.edu
### Jimmie Gilmer - 
