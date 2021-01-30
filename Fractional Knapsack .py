#User function Template for python3
def fractionalknapsack(W,Items,n):
    '''
    :param W: max weight which can be stored
    :param Items: List contianing Item class objects as defined in driver code, with value and weight
    :param n: size of Items
    :return: Float value of max possible value, two decimal place accuracy is expected by driver code
    
    {
        class Item:
        def __init__(self,val,w):
            self.value = val
            self.weight = w
    }
    '''
    Items.sort(key=lambda x : x.value/x.weight,reverse=True)
    ans = 0
    for i in range(n):
        if W == 0:
            return ans
        if W > Items[i].weight:
            ans += Items[i].value
            W -= Items[i].weight
        elif Items[i].weight > W:

            fract = W
            ans += fract*(Items[i].value/Items[i].weight)
            W -= fract
        else:
            return ans
    return ans
    
