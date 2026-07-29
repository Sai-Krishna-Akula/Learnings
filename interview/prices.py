from typing import List
def daily_prices(prices:List) -> List:

    n = len(prices)
    result = []
    for i in range(n):
        for j in range(i, n):
            if prices[i] < prices[j]:
                result.append(j - i)
                break
    
    return result         



if __name__ == "__main__":
    prices = [73, 74, 75, 71, 69, 72, 76, 73]
    print(daily_prices(prices))

    # print(daily_prices([10, 10, 10])

    # print(daily_prices[30, 10, 20, 60 ])