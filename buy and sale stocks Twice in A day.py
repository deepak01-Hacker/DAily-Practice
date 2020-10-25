#Maximum Profit 
def ans(price,n):
    buy1,buy2 = 10**7,10**7
    profit1 , profit2 = 0,0
    for i in range(n): 
        buy1 = min(buy1,price[i])
        profit1 = max(profit1,price[i]-buy1)
        buy2 = min(buy2,price[i]-profit1)
        profit2 = max(profit2,price[i]-buy2)
    return profit2

if __name__ == "__main__":
    arr = [10,22,5,75,65,80]
    #ANs = 87    
    print(ans(arr,len(arr)))
