def stock_maximization(max, company_list):
    best = None                                                                               #O(1)

    for candidate in stock_combinations(company_list):                                        #O(2^n)
        if verify_combinations(max, candidate):                                               #O(m)
            if best is None or total_stocks(candidate) > total_stocks(best):                  #O(2m) -> O(m)
                best = candidate                                                              #O(1)

    stocks = 0                                                                                #O(1)
    for i in range(len(best)):                                                                #O(b), b == number of companies in best
        stocks += best[i][0] # Counting the number of stocks                                  #O(1)
    return stocks                                                                             #O(1)
                                                                                              #Time Complexity: O(2^n * m), n == # of companies, m == # of elems in combinations

def stock_combinations(items):
    n = len(items)                                                                            #O(1)
    for i in range(1 << n):                                                                   #O(2^n), where n is the number of items
        combination = [items[j] for j in range(n) if (i & (1 << j)) != 0]                     #O(n)
        yield combination                                                                     #O(1)
                                                                                              #Time Complexity: O(2^n * n) -> O(2^n)

def verify_combinations(max, candidate):
    total_cost = 0                                                                            #O(1)
    for item in candidate:                                                                    #O(m), m == # of candiates
        total_cost += item[1] # Sum the cost of the candidate                                 #O(1)
    if total_cost <= max:                                                                     #O(1)
        return True                                                                           #O(1)
    else:
        return False                                                                          #O(1)
                                                                                              #Time Complexity: O(m + 5(1)) == O(m)

def total_stocks(candidate):
    total = 0                                                                                 #O(1)
    for item in candidate:                                                                    #O(m), m == # of candidates
        total += item[0]                                                                      #O(1)
    return total                                                                              #O(1)
                                                                                              #Time Complexity: O(m + 4(1)) == O(m)

if __name__ == "__main__":
    with open("output1.txt", "w") as Outfile:                                                  #O(1)                 
        with open('input.txt') as file:                                                       #O(1)
            
            # 1 different inputs
            for i in range(10):                                                               #O(N), N == 10       
                # Reads the max amount
                max_amount = int(file.readline().strip())                                     #O(1)
                temp = file.readline().strip()[1:-1].split("],[")                             #O(1) + 2O(l), with l == length of line = O(l)
                companies = []                                                                #O(1)
                for j in temp:                                                                #O(k) -> k == number of companies
                    if j == '': # Company Stock list is empty ([x, y] > 0)                    #O(1)
                        continue                                                              #O(1)
                        '''
                        Cuurent code will allow for an empty company in the input list, but if this isn't desired, delete the continue
                        and uncomment this code:
                        companies = []                                                        #O(1)
                        #break
                        '''                                                             
                    stocks, value = j.split(",")                                              #O(1)
                    stocks = int(stocks)                                                      #O(1)
                    value = int(value)                                                        #O(1)
                    companies.append([stocks, value])                                         #O(1)
                
                # Constraint check
                if len(companies) >= 0 and len(companies) <= 100000:                          #O(1)
                    # Output 1
                    number_of_stocks = stock_maximization(max_amount, companies)              #O(2^n * m)
                    Outfile.write(f"Input {i + 1}: Number of stocks = {number_of_stocks}\n")  #O(1)
                else:
                    Outfile.write("Sorry, this input is invalid.\n")                          #O(1)
            print("\nResults written to output.txt\n")                                        #O(1)
                                                                                              #Time Complexity: O(N(2^n * m)) == O(10(2^n * m)) -> O(2^n)
                            