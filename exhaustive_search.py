def stock_maximization(max, company_list):
    best = None

    for candidate in stock_combinations(company_list):
        if verify_combinations(max, candidate):
            if best is None or total_stocks(candidate) > total_stocks(best):
                best = candidate

    stocks = 0
    for i in range(len(best)):
        stocks += best[i][0] # Counting the number of stocks
    return stocks

def stock_combinations(items):
    n = len(items)
    for i in range(1 << n):
        combination = [items[j] for j in range(n) if (i & (1 << j)) != 0]
        yield combination

def verify_combinations(max, candidate):
    total_cost = 0
    for item in candidate:
        total_cost += item[1] # Sum the cost of the candidate
    if total_cost <= max:
        return True
    else:
        return False

def total_stocks(candidate):
    total = 0
    for item in candidate:
        total += item[0]
    return total


if __name__ == "__main__":
    with open("output1.txt", "w") as Outfile:                                                              
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
                    companies.append([stocks, value])
                
                # Constraint check
                if len(companies) >= 0 and len(companies) <= 100000:
                    # Output 1
                    number_of_stocks = stock_maximization(max_amount, companies)
                    Outfile.write(f"Input {i + 1}: Number of stocks = {number_of_stocks}\n")
                else:
                    Outfile.write("Sorry, this input is invalid.\n")
            print("\nResults written to output1.txt\n")                      

                            