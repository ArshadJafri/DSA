def stock(arr):


    profit =0
    buy = arr[0]

    for sell in arr[1:]:

        print("sell herre",sell)
        print("buy here",buy)
        if sell > buy:
            profit = max(profit,sell-buy)
            print("profit",profit)
        
        else:
            buy = sell
            print("buy",buy)
            print("sell",sell)

    return profit

print(stock([7,6,4,3,1])) 
