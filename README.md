# Stock Purchase Maximization

## Exhaustive Search
(`stock_maximization.py`) maximizes the number of stocks that can be bought with a given amount of money. It explores all possible combinations of stocks from different companies and returns the combination that maximizes the total number of stocks without exceeding the specified amount.

## Dynamic Approach
(`max_stocks_dynamic.py`) finds the maximum number of stocks you can buy with a given amount of money. It explores all possible subset of stocks and returns the maximum number of stocks that can be bought without exceeding the specified amount.

## Usage

1. **Input:**
    - Create a text file (`input.txt`) with the following format:
        ```
        max_amount1
        [stocks1, value1], [stocks2, value2], ...
        max_amount2
        [stocks1, value1], [stocks2, value2], ...
        ...
        ```
        Each block represents a test case, where `max_amount` is the maximum amount of money, and the list represents stocks for different companies.

    - Ensure that the input follows the constraints:
        - 0 <= len(companies) <= 100000

2. **Run the script:**
    - Execute the script in your Python environment.
    ```bash
    python <stock_maximization_script>.py
    ```

3. **Output:**
    - The script will write the results to an output file (`output1.txt`).
    - The output file will contain lines like:
        ```
        Input 1: Number of stocks = <number_of_stocks>
        Input 2: Number of stocks = <number_of_stocks>
        ...
        ```
        Or, if the input is invalid:
        ```
        Sorry, this input is invalid.
## Example

For the provided `input.txt`:
```plaintext
10
[1, 2], [4, 3], [5, 6], [6, 7]
20
[2, 3], [3, 4], [4, 5]
```

### Alan Campos - argelalan@csu.fullerton.edu
### Jimmie Gilmer - 
